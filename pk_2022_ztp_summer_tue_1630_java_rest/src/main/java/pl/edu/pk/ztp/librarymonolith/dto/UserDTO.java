package pl.edu.pk.ztp.librarymonolith.dto;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;

import java.util.Arrays;
import java.util.List;

@JsonPropertyOrder({"id", "username", "roles"})
@JsonInclude(JsonInclude.Include.NON_NULL)
public class UserDTO {

    private Integer id;
    private String username;
    private List<String> roles;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public List<String> getRoles() {
        return roles;
    }

    public void setRoles(List<String> roles) {
        this.roles = roles;
    }

    public static UserDTO create(final int id, final String name, final String roles){
        final UserDTO newUser = new UserDTO();
        newUser.setId(id);
        newUser.setUsername(name);
        if(roles != null){
            newUser.setRoles(Arrays.asList(roles.split(",", -1)));
        }
        return newUser;
    }
}