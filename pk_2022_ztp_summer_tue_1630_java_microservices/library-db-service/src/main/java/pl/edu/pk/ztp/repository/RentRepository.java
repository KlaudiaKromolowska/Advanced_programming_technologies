package pl.edu.pk.ztp.repository;

import org.springframework.data.repository.CrudRepository;
import pl.edu.pk.ztp.dto.Book;
import pl.edu.pk.ztp.dto.Rent;
import pl.edu.pk.ztp.dto.User;

import java.util.List;

public interface RentRepository extends CrudRepository<Rent, Integer> {
    List<Rent> findAllByUser(User user);
    List<Rent> findAllRentByBookAndUserAndReturnDateIsNull(Book book, User user);
    List<Rent> findAllByBook(Book book);
}
