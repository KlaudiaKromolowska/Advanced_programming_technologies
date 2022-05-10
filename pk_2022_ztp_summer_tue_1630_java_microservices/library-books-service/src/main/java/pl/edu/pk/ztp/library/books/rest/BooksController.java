package pl.edu.pk.ztp.library.books.rest;

import com.netflix.appinfo.InstanceInfo;
import com.netflix.discovery.EurekaClient;
import org.apache.http.HttpHeaders;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.reactive.function.client.WebClient;
import org.springframework.web.server.ResponseStatusException;
import reactor.core.publisher.Mono;

@RestController
@RequestMapping(value = "/books", produces = MediaType.APPLICATION_JSON_VALUE)
public class BooksController {

    @Autowired
    private EurekaClient client;

    @GetMapping
    public Mono<String> getBooks() {
        return getLibraryDbServiceWebClient().get().uri("/internal/books").retrieve().bodyToMono(String.class);
    }

    @GetMapping("/{id}")
    public Mono<String> getBookRentals(@PathVariable Integer id) {
        return getLibraryDbServiceWebClient().get().uri("/internal/books/" + id).retrieve().onStatus(HttpStatus::isError, response -> Mono.error(new ResponseStatusException(response.statusCode(), "DB error"))).bodyToMono(String.class);
    }

    @PatchMapping("/rent/{id}")
    public Mono<String> rentABook(@PathVariable Integer id, @RequestHeader(value = "user", required = false) final Integer userID) {
        if (userID == null) {
            throw new ResponseStatusException(HttpStatus.UNAUTHORIZED, "Missing userID");
        }
        return getLibraryDbServiceWebClient().patch().uri("/internal/books/rent/" + id).header("user", String.valueOf(userID)).retrieve().onStatus(HttpStatus::isError, response -> Mono.error(new ResponseStatusException(response.statusCode(), "DB error"))).bodyToMono(String.class);
    }

    @PatchMapping("/return/{id}")
    public Mono<String> returnABook(@PathVariable Integer id, @RequestHeader Integer userID) {
        return getLibraryDbServiceWebClient().patch().uri("/internal/books/return/" + id).header("user", String.valueOf(userID)).retrieve().onStatus(HttpStatus::isError, response -> Mono.error(new ResponseStatusException(response.statusCode(), "DB error"))).bodyToMono(String.class);
    }

    private WebClient getLibraryDbServiceWebClient() {
        InstanceInfo service = client.getApplication("library-db-service").getInstances().get(0);
        return WebClient.builder().baseUrl(String.format("http://%s:%s", service.getHostName(), service.getPort())).defaultHeader(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE).build();
    }

}
