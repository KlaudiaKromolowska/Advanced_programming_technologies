package pl.edu.pk.ztp.repository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;
import pl.edu.pk.ztp.dto.User;

@Repository
public interface UserRepository extends CrudRepository<User, Integer> {
    User findUserById(Integer id);
}
