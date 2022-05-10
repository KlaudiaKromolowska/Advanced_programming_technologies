package pl.edu.pk.ztp.dto;

import lombok.Builder;
import lombok.Data;

import java.util.List;

@Data
@Builder
public class UserDTO {
    Integer id;
    String username;
    List<String> roles;

    @Override
    public String toString() {
        return "{\n" + "\t\"id\":\"" + id + "\"," + "\t\"username\":\"" + username + "\"," + "\t\"roles\":\"" + roles + "\"" + '}';
    }
}
