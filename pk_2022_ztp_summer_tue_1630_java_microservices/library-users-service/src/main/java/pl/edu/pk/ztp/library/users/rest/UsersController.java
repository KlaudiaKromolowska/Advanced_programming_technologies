package pl.edu.pk.ztp.library.users.rest;

import com.netflix.appinfo.InstanceInfo;
import com.netflix.discovery.EurekaClient;
import org.apache.http.HttpHeaders;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.reactive.function.BodyInserters;
import org.springframework.web.reactive.function.client.WebClient;
import org.springframework.web.server.ResponseStatusException;
import reactor.core.publisher.Mono;

@RestController
@RequestMapping(value = "users", produces = MediaType.APPLICATION_JSON_VALUE)
public class UsersController {

    @Autowired
    private EurekaClient client;

    @GetMapping
    Mono<String> getAllUsers() {
        final WebClient webClient = getLibraryDbServiceWebClient();
        return webClient.get().uri("/internal/users").retrieve().bodyToMono(String.class);
    }

    @GetMapping("/{userID}")
    Mono<String> getUserById(@PathVariable final Integer userID) {
        final WebClient webClient = getLibraryDbServiceWebClient();
        return webClient.get().uri("/internal/users/" + userID).retrieve().onStatus(HttpStatus::isError, response -> Mono.error(new ResponseStatusException(response.statusCode(), "DB error"))).bodyToMono(String.class);
    }

    @DeleteMapping("/{userID}")
    Mono<String> deleteUser(@PathVariable final Integer userID) {
        if (userID == null) {
            throw new ResponseStatusException(HttpStatus.NOT_FOUND, "Missing user");
        }
        final WebClient webClient = getLibraryDbServiceWebClient();
        try {
            return webClient.delete().uri("/internal/users/" + userID).retrieve().onStatus(HttpStatus::isError, response -> Mono.error(new ResponseStatusException(response.statusCode(), "DB error"))).bodyToMono(String.class);
        } catch (Exception e) {
            return Mono.just(e.getMessage());
        }
    }

    @PostMapping()
    Mono<String> postUser(@RequestBody final String user) {
        final WebClient webClient = getLibraryDbServiceWebClient();
        return webClient.post().uri("/internal/users").body(BodyInserters.fromPublisher(Mono.just(user), String.class)).retrieve().onStatus(HttpStatus::isError, response -> Mono.error(new ResponseStatusException(response.statusCode(), "DB error"))).bodyToMono(String.class);
    }

    private WebClient getLibraryDbServiceWebClient() {
        InstanceInfo service = client.getApplication("library-db-service").getInstances().get(0);
        return WebClient.builder().baseUrl(String.format("http://%s:%s", service.getHostName(), service.getPort())).defaultHeader(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE).build();
    }
}



