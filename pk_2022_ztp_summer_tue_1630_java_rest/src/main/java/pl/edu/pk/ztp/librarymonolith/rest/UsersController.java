package pl.edu.pk.ztp.librarymonolith.rest;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.server.ResponseStatusException;
import pl.edu.pk.ztp.librarymonolith.dto.UserDTO;
import pl.edu.pk.ztp.librarymonolith.repository.UserRepository;

import java.util.List;

@RestController
@RequestMapping("/users")
public class UsersController {
    final UserRepository userRepository;

    public UsersController(final UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @GetMapping
    public List<UserDTO> getAllUsers() {
        return userRepository.findAll();
    }

    @GetMapping("/{id}")
    public UserDTO getUserById(@PathVariable("id") final Integer userID) {
        try {
            return userRepository.findByUserId(userID);
        } catch (Exception e) {
            throw new ResponseStatusException(HttpStatus.NOT_FOUND, "There is no user with this ID", e);
        }
    }

    @DeleteMapping("/{id}")
    public void deleteUser(@PathVariable("id") final Integer userID) {
        try {
            if (!userRepository.deleteUserById(userID)) {
                throw new ResponseStatusException(HttpStatus.NOT_FOUND, "There is no user with this ID");
            }
        } catch (final UnsupportedOperationException e) {
            throw new ResponseStatusException(HttpStatus.FORBIDDEN, e.getMessage(), e);
        }
    }

    @PostMapping
    public UserDTO postUser(@RequestBody final UserDTO user) {
        return userRepository.createUser(user);
    }
}

