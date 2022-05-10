package pl.edu.pk.ztp.rest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import pl.edu.pk.ztp.dto.*;
import pl.edu.pk.ztp.repository.BookRepository;
import pl.edu.pk.ztp.repository.RentRepository;
import pl.edu.pk.ztp.repository.UserRepository;

import java.sql.Date;
import java.util.List;
import java.util.Optional;

@RestController
@ResponseBody
@RequestMapping("/internal/books")
public class BookController {

    @Autowired
    BookRepository bookRepository;

    @Autowired
    RentRepository rentRepository;

    @Autowired
    UserRepository userRepository;

    @GetMapping
    public ResponseEntity<List<Book>> getBooks() {
        return new ResponseEntity(bookRepository.findAll(), HttpStatus.OK);
    }

    @GetMapping("/{id}")
    public ResponseEntity<Object> getBookRentals(@PathVariable Integer id) {
        Optional<Book> bookOpt = bookRepository.findById(id);
        if (bookOpt.isEmpty()) {
            return new ResponseEntity<>("There is no book with this ID", HttpStatus.BAD_REQUEST);
        }
        Book book = bookOpt.get();
        List<Rent> rents = rentRepository.findAllByBook(book);

        return new ResponseEntity<>(RentResponse.RentResponseCreator(RentResponseDTO.builder().rentals(rents).author(book.getAuthor()).title(book.getTitle()).quantity(book.getQuantity()).id(book.getId()).build()), HttpStatus.OK);
    }

    @PatchMapping("/rent/{id}")
    public ResponseEntity<Object> rentABook(@PathVariable Integer id, @RequestHeader Integer user) {
        Optional<Book> bookOpt = bookRepository.findById(id);
        if (bookOpt.isEmpty()) {
            return new ResponseEntity<>("There is no book with this ID", HttpStatus.BAD_REQUEST);
        }
        Book book = bookOpt.get();
        List<Rent> rents = rentRepository.findAllByBook(book);
        long activeRents = rents.stream().filter(rent -> rent.getReturnDate() == null).count();
        User rentingPerson = userRepository.findUserById(user);
        if (user == null) {
            return new ResponseEntity<>("There is no user with this ID", HttpStatus.UNAUTHORIZED);
        }
        Date date = new Date(new java.util.Date().getTime());
        if (activeRents < book.getQuantity()) {
            Rent savedRent = rentRepository.save(new Rent(rentingPerson, book, date, null));
            return new ResponseEntity<>(RentResponseDTO.builder().rentals(List.of(savedRent)).author(book.getAuthor()).title(book.getTitle()).quantity(book.getQuantity()).id(book.getId()).build(), HttpStatus.CREATED);
        } else {
            return new ResponseEntity<>("You cannot rent this book", HttpStatus.CONFLICT);
        }

    }

    @PatchMapping("/return/{id}")
    public ResponseEntity<Object> returnABook(@PathVariable Integer id, @RequestHeader Integer user) {
        User returningUser = userRepository.findUserById(user);
        if (user == null) {
            return new ResponseEntity<>("There is no user with this ID", HttpStatus.UNAUTHORIZED);
        }
        Optional<Book> bookOpt = bookRepository.findById(id);
        if (bookOpt.isEmpty()) {
            return new ResponseEntity<>("There is no book with this ID", HttpStatus.BAD_REQUEST);
        }
        Book book = bookOpt.get();
        List<Rent> currentRents = rentRepository.findAllRentByBookAndUserAndReturnDateIsNull(book, returningUser);
        Rent currentRent = null;

        if (currentRents != null) {
            if (!currentRents.isEmpty()) {
                currentRent = currentRents.get(0);
            }
        }
        if (currentRent == null) {
            return new ResponseEntity<>("This user did not rent this book", HttpStatus.UNAUTHORIZED);
        }

        Date date = new Date(new java.util.Date().getTime());
        currentRent.setReturnDate(date);
        currentRent = rentRepository.save(currentRent);
        return new ResponseEntity<>(RentResponseDTO.builder().rentals(List.of(currentRent)).author(book.getAuthor()).title(book.getTitle()).quantity(book.getQuantity()).id(book.getId()).build(), HttpStatus.CREATED);
    }
}
