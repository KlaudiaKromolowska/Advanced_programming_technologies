package pl.edu.pk.ztp.dto;


import pl.edu.pk.ztp.dto.User;
import pl.edu.pk.ztp.dto.UserDTO;

import java.util.Arrays;

public class UserDTOConv {
    public static UserDTO convert(User user) {
        String roles = user.getRoles();
        String[] roleArr = roles.split(",");
        return UserDTO.builder()
                .id(user.getId())
                .username(user.getName())
                .roles(Arrays.asList(roleArr))
                .build();

    }

    public static User convert(UserDTO userDTO) {
        User user = new User();
        StringBuilder stringBuilder = new StringBuilder();
        userDTO.getRoles().forEach(role -> stringBuilder.append(role).append(","));
        stringBuilder.deleteCharAt(stringBuilder.length() - 1);

        user.setName(userDTO.getUsername());
        user.setRoles(stringBuilder.toString());
        if (userDTO.getId() != null) {
            user.setId(userDTO.getId());
        }
        return user;
    }
}
