package pl.edu.pk.ztp.librarymonolith.repository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;
import org.springframework.web.server.ResponseStatusException;
import pl.edu.pk.ztp.librarymonolith.dto.BookDTO;
import pl.edu.pk.ztp.librarymonolith.dto.BookRentalDTO;
import pl.edu.pk.ztp.librarymonolith.dto.UserDTO;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

@Repository
public class BookRepository {


    private final JdbcTemplate jdbcTemplate;

    @Autowired
    public BookRepository(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }

    public List<BookDTO> findAll(boolean showAvailable){
        if(showAvailable){
            return jdbcTemplate.query("SELECT * FROM tbl_books WHERE id NOT IN (" +
                    "SELECT DISTINCT tbl_books.id FROM tbl_books JOIN tbl_rentals ON (tbl_books.id = tbl_rentals.bookid_fk) " +
                    "WHERE return_date IS NULL GROUP BY tbl_books.id HAVING tbl_books.quantity <= count(*))",
                    BookRepository::mapResultsToBookDTO);
        }
        else return jdbcTemplate.query("SELECT * FROM tbl_books",
                BookRepository::mapResultsToBookDTO);
    }

    public boolean isBookAvailable(final Integer bookID) {
        return jdbcTemplate.queryForObject("SELECT COUNT(*) FROM TBL_RENTALS WHERE bookid_fk =? AND return_date IS NULL", Integer.class, bookID) <
                jdbcTemplate.queryForObject("SELECT QUANTITY FROM TBL_BOOKS WHERE id = ?", Integer.class, bookID);
    }

    public BookDTO findBookById(final Integer bookID){
        try {
            return jdbcTemplate.queryForObject("SELECT * FROM tbl_books WHERE id = ?", BookRepository::mapResultsToBookDTO, bookID);
        }catch (final Exception e) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "Missing book", e);
        }
    }

    public List<BookRentalDTO> findRentalByBookId(final Integer bookID) {
        return jdbcTemplate.query("SELECT tbl_rentals.*, tbl_users.name FROM tbl_rentals JOIN tbl_users ON tbl_rentals.userid_fk = tbl_users.id WHERE BOOKID_FK = ?", BookRepository::mapResultsToBookRentalDTO, bookID);
    }


    public boolean returnBook(final Integer bookId, final Integer userID) {
        return jdbcTemplate.update("UPDATE tbl_rentals SET return_date = CURRENT_DATE() WHERE bookid_fk = ?  AND userid_fk = ? AND return_date IS NULL", bookId, userID) ==1;
    }
    public boolean rentBook(final Integer bookID, final Integer userID) {
        return jdbcTemplate.update("INSERT INTO tbl_rentals (userid_fk, bookid_fk, rental_date) VALUES(?, ?, CURRENT_DATE())", userID, bookID) ==1;
    }

    static BookDTO mapResultsToBookDTO(ResultSet rs, int rowNum) throws SQLException{
        return BookDTO.create(rs.getInt("id"), rs.getString("author"),
                rs.getString("title"), rs.getInt("quantity"));
    }

    static BookRentalDTO mapResultsToBookRentalDTO(ResultSet rs, int rowNum) throws SQLException{
        UserDTO user = UserDTO.create(rs.getInt("userid_fk"), rs.getString("name"), null);
        return BookRentalDTO.create(rs.getInt("id"), rs.getDate("rental_date"), rs.getDate("return_date"), user);
    }
//    private static Date getAsJavaDate(final ResultSet rs, final String name) throws  SQLException{
//        final java.sql.Date sqlDate = rs.getDate(name);
//        return sqlDate == null ? null : new Date(sqlDate.getTime())
//    }

}