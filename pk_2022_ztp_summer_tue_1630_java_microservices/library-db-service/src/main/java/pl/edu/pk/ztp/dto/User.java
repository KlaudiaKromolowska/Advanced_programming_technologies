package pl.edu.pk.ztp.dto;


import lombok.Data;
import lombok.RequiredArgsConstructor;

import javax.persistence.*;
import java.io.Serializable;
import java.util.List;

@Table(name = "tbl_users")
@Entity
@RequiredArgsConstructor
@Data
public class User implements Serializable {
    @Id
    @GeneratedValue
    Integer id;
    String name;
    String roles;
    @OneToMany(fetch = FetchType.EAGER, orphanRemoval = true, cascade = CascadeType.REMOVE)
    List<Rent> rents;
}
