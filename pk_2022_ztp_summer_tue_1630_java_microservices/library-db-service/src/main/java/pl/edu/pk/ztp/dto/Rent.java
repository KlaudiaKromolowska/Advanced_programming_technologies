package pl.edu.pk.ztp.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.lang.NonNull;

import javax.persistence.*;
import java.io.Serializable;
import java.sql.Date;


@Table(name = "tbl_rentals")
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Data
public class Rent implements Serializable {
    @Id
    @GeneratedValue
    Integer id;

    @OneToOne(fetch = FetchType.EAGER)
    User user;

    @OneToOne(fetch = FetchType.EAGER)
    Book book;

    @NonNull
    @Column(name = "rental_date")
    Date rental;

    @Column(name = "return_date")
    Date returnDate;

    public Rent(User user, Book book, @NonNull Date rental, Date returnDate) {
        this.user = user;
        this.book = book;
        this.rental = rental;
        this.returnDate = returnDate;
    }
}
