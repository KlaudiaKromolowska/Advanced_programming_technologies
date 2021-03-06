package pl.edu.pk.ztp;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

@SpringBootApplication
@EnableDiscoveryClient
public class LibraryDbServiceApplication {

    public static void main(String[] args) {
        SpringApplication.run(LibraryDbServiceApplication.class, args);
    }

}
