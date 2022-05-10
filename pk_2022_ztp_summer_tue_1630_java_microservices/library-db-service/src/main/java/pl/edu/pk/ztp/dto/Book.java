package pl.edu.pk.ztp.dto;

import lombok.Data;
import lombok.RequiredArgsConstructor;

import javax.persistence.*;
import java.io.Serializable;
import java.util.List;

@Table(name = "tbl_books")
@Entity
@RequiredArgsConstructor
@Data
public class Book implements Serializable {
    @Id
    @GeneratedValue
    Integer id;
    String title;
    String author;
    Integer quantity;
    @OneToMany(fetch = FetchType.EAGER)
    List<Rent> rents;
}
