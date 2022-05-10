package pl.edu.pk.ztp.dto;

import lombok.Builder;
import lombok.Data;

import java.sql.Date;

@Data
@Builder
public class RentDTO {
    UserDTO user;
    Book book;
    Date rentalDate;
    Date returnDate;
}
