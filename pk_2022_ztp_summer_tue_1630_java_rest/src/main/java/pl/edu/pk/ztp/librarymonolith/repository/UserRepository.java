package pl.edu.pk.ztp.librarymonolith.repository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.support.GeneratedKeyHolder;
import org.springframework.jdbc.support.KeyHolder;
import org.springframework.stereotype.Repository;
import pl.edu.pk.ztp.librarymonolith.dto.UserDTO;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

@Repository
public class UserRepository {


    private final JdbcTemplate jdbcTemplate;

    @Autowired
    public UserRepository(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }

    public List<UserDTO> findAll(){
        return jdbcTemplate.query("SELECT * FROM tbl_users",
                UserRepository::mapResultsToUserDTO);
    }

    public UserDTO findByUserId(final Integer userID){
        return jdbcTemplate.queryForObject("SELECT * FROM tbl_users WHERE id = ?",
                UserRepository::mapResultsToUserDTO, userID);
    }

    public boolean deleteUserById(final Integer userID){
        if(jdbcTemplate.queryForObject("SELECT count(*) FROM tbl_rentals WHERE userid_fk = ? AND return_date IS NULL", Integer.class, userID) != 0){
            throw new UnsupportedOperationException("Cannot remove user with rented books");
        }
        return jdbcTemplate.update("DELETE tbl_users where id = ?", userID) == 1;
    }

    public UserDTO createUser(final UserDTO user){
        String query = "INSERT INTO tbl_users (name, roles) VALUES (?, ?)";
        final KeyHolder keyHolder = new GeneratedKeyHolder();
        jdbcTemplate.update(connection -> {
            PreparedStatement insert= connection.prepareStatement(query, new String[]{"id"});
            insert.setString(1, user.getUsername());
            insert.setString(2, String.join(",", user.getRoles()));
            return insert;
        }, keyHolder);
        user.setId(keyHolder.getKey().intValue());
        return user;
    }

    public static UserDTO mapResultsToUserDTO(ResultSet rs, int rowNum) throws SQLException{
        return UserDTO.create(rs.getInt("id"),
                rs.getString("name"),
                rs.getString("roles"));
    }
}
