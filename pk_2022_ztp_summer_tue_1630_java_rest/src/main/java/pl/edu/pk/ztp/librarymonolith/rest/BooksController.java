package pl.edu.pk.ztp.librarymonolith.rest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.server.ResponseStatusException;
import pl.edu.pk.ztp.librarymonolith.dto.BookDTO;
import pl.edu.pk.ztp.librarymonolith.repository.BookRepository;
import pl.edu.pk.ztp.librarymonolith.repository.UserRepository;

import java.util.List;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/books")
public class BooksController {
    private final BookRepository bookRepository;
    private final UserRepository userRepository;

    @Autowired
    public BooksController(final BookRepository bookRepository, final UserRepository userRepository) {
        this.bookRepository = bookRepository;
        this.userRepository = userRepository;
    }

    @GetMapping
    public List<BookDTO> getAllBooks(@RequestParam(value = "available", required = false) final boolean showOnlyAvailable){
        return bookRepository.findAll(showOnlyAvailable);
    }

    @GetMapping("/{id}")
    public BookDTO getBookRentals(@PathVariable("id") final Integer bookID){
        try {
            final BookDTO book = bookRepository.findBookById(bookID);
            book.setRentals(bookRepository.findRentalByBookId(bookID));
            return book;
        } catch (final Exception e) {
            throw new ResponseStatusException(HttpStatus.NOT_FOUND, "There is no book with this ID", e);
        }
    }

    @PatchMapping("/return/{id}")
    public BookDTO patchReturnBook(@PathVariable("id") final Integer bookID, @RequestHeader(value = "user", required = false) final Integer userID){
        if (userID == null) {
            throw new ResponseStatusException(HttpStatus.UNAUTHORIZED, "Missing user");
        }
        try {
            userRepository.findByUserId(userID);
        } catch (final Exception e) {
            throw  new ResponseStatusException(HttpStatus.UNAUTHORIZED, "Missing user", e);
        }
        final BookDTO book = bookRepository.findBookById(bookID);
        if(!bookRepository.returnBook(bookID, userID)) {

            throw new ResponseStatusException(HttpStatus.CONFLICT, "Cannot return book");
        }
        book.setRentals(bookRepository.findRentalByBookId(bookID)
                .stream().filter(x -> userID.equals(x.getUser().getId())).collect(Collectors.toList()));
        return book;
    }


    @PatchMapping("/rent/{id}")
    public BookDTO patchRentBook(@PathVariable("id") final Integer bookID, @RequestHeader(value = "user", required = false) final Integer userID) {
        if (userID == null) {
            throw new ResponseStatusException(HttpStatus.UNAUTHORIZED, "Missing user");
        }
        try {
            userRepository.findByUserId(userID);
        } catch (final Exception e) {
            throw  new ResponseStatusException(HttpStatus.UNAUTHORIZED, "Missing user", e);
        }
        if (!bookRepository.isBookAvailable(bookID)) {
            throw new ResponseStatusException(HttpStatus.CONFLICT, "This book is not available");
        }
        final BookDTO book = bookRepository.findBookById(bookID);
        if(!bookRepository.rentBook(bookID, userID)) {
            throw new ResponseStatusException(HttpStatus.CONFLICT, "Cannot rent book");
        }

        book.setRentals(bookRepository.findRentalByBookId(bookID)
                .stream().filter(x -> userID.equals(x.getUser().getId())).collect(Collectors.toList()));
        return book;
    }


}