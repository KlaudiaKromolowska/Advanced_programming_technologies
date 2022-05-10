package pl.edu.pk.ztp.dto;

import lombok.Builder;
import lombok.Data;
import pl.edu.pk.ztp.dto.Rent;

import java.io.Serializable;
import java.util.List;

@Builder
@Data
public class RentResponseDTO implements Serializable {
    Integer id;
    String title;
    String author;
    Integer quantity;
    List<Rent> rentals;
}
