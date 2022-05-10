package pl.edu.pk.ztp.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class RentResponse {
    Integer id;
    String title;
    String author;
    Integer quantity;
    List<Rent> rentals;

    public static RentResponse RentResponseCreator(RentResponseDTO dto) {
        return new RentResponse(dto.getId(), dto.getTitle(), dto.getAuthor(), dto.getQuantity(), dto.getRentals());
    }

}
