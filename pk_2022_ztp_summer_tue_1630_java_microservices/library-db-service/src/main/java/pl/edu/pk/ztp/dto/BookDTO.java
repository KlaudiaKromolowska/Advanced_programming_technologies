package pl.edu.pk.ztp.dto;

import lombok.Builder;
import lombok.Data;

@Data
@Builder
public class BookDTO {
    int id;
    String title;
    String author;
    int quantity;
}
