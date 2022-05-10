package pl.edu.pk.ztp.rest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import pl.edu.pk.ztp.dto.Rent;
import pl.edu.pk.ztp.dto.User;
import pl.edu.pk.ztp.dto.UserDTO;
import pl.edu.pk.ztp.repository.RentRepository;
import pl.edu.pk.ztp.repository.UserRepository;
import pl.edu.pk.ztp.dto.UserDTOConv;

import java.util.List;
import java.util.stream.Collectors;

@RestController
@ResponseBody
@RequestMapping("/internal/users")
public class UserController {

    @Autowired
    UserRepository userRepository;

    @Autowired
    RentRepository rentRepository;

    @PostMapping
    public ResponseEntity<UserDTO> addUser(@RequestBody UserDTO userDTO) {
        User user = UserDTOConv.convert(userDTO);
        try {
            user = userRepository.save(user);
        } catch (Exception e) {
            return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
        }
        return new ResponseEntity<>(UserDTOConv.convert(user), HttpStatus.CREATED);
    }

    @GetMapping
    public ResponseEntity<List<UserDTO>> getUsers() {
        List<User> users = (List<User>) userRepository.findAll();

        return new ResponseEntity<>(users.stream()
                .map(UserDTOConv::convert)
                .collect(Collectors.toList()), HttpStatus.OK);
    }

    @GetMapping("/{id}")
    public ResponseEntity<Object> getUser(@PathVariable Integer id) {

        if (id == null) {
            return new ResponseEntity<>("There is no user with this ID", HttpStatus.NOT_FOUND);
        }

        User user = userRepository.findUserById(id);
        if (user == null) {
            return new ResponseEntity<>("Wrong ID number", HttpStatus.BAD_REQUEST);
        }

        return new ResponseEntity<>(UserDTOConv.convert(user), HttpStatus.OK);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<String> deleteUser(@PathVariable Integer id) {
        if (id == null) {
            return new ResponseEntity("Wrong ID number", HttpStatus.BAD_REQUEST);
        }
        User user = userRepository.findUserById(id);
        if (user == null) {
            return new ResponseEntity("There is no user with this ID", HttpStatus.BAD_REQUEST);
        }
        List<Rent> rents = rentRepository.findAllByUser(user);
        long numOfRentedBooks = rents.stream().filter(rent -> rent.getReturnDate() == null).count();
        if (numOfRentedBooks != 0) {
            return new ResponseEntity("This user has books which he/she should return before removing from database.", HttpStatus.FORBIDDEN);
        }
        List<Rent> oldRents = rentRepository.findAllByUser(user);
        rentRepository.deleteAll(oldRents);
        userRepository.deleteById(id);
        return new ResponseEntity("User has been deleted.", HttpStatus.OK);
    }

}
