package pl.edu.pk.ztp.dto;


import pl.edu.pk.ztp.dto.Book;
import pl.edu.pk.ztp.dto.BookDTO;

public class BookDTOConv {
    public static Book convert(BookDTO bookDTO) {
        Book book = new Book();
        book.setAuthor(bookDTO.getAuthor());
        book.setQuantity(bookDTO.getQuantity());
        book.setTitle(bookDTO.getTitle());
        return book;
    }

    public static BookDTO convert(Book book) {
        return BookDTO.builder()
                .author(book.getAuthor())
                .quantity(book.getQuantity())
                .title(book.getTitle())
                .id(book.getId())
                .build();
    }
}
