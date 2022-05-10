# L04: Zaawansowane techniki programowania

Celem zadania będzie przygotowanie aplikacji do obsługi biblioteki opartej o archtiekturę mikroserwisową przy wykorzystaniu frameworku Spring Boot i języka Java.

## Przygotowanie

Przed zajęciami proszę o zapoznanie się z [załączonymi materiałami](docs/introduction.md).
W przypadku braku znajomości języka SQL polecam zapoznanie się z [dodatkowymi materiałami pomocniczymi](docs/sql_cheetsheet.md) wymaganymi do realizacji komunikacji z bazą danych.

## Wymagania funkcjonalne aplikacji

1. Zasoby i funkcjonalność powinny być udostępniane przez REST API zgodne z dokumentacją zawartą w [docs/library-rest-service.yaml](https://epam-online-courses.github.io/ZTP-Java-REST-Monolith/).
1. Aplikacja powinna wykorzystywać wbudowaną bazę danych H2 do przechowywania stanu systemu.

## Wymagania dotyczące architektury aplikacji

1. Aplikacja powinna składać się z 3 usług odpowiedzialnych za funkcjonalność aplikacji oraz 1 procesu pełniącego rolę rejestru dostępnych usług. 
   * Usługa rejestru oparta o Spring Eureka powinna być dostępna pod adresem [http://localhost:8761/](http://localhost:8761/)
   * Usługa umożliwiająca dostęp do bazy danych powinna być dostępna pod losowym portem
   * Usługa umożliwiająca dostęp do zasobu `/users` powinna być dostępna pod losowym portem
   * Usługa umożliwiająca dostęp do zasobu `/books` powinna być dostępna pod losowym portem
1. Usługi odpowiedzialne za funkcjonalność aplikacji powinny rejestrować się w Eureka Discovery oraz dynamicznie pobierać informację na temat dostępności innych usług
1. Usługi umożliwiające dostęp do zasobów `/users` oraz `/books` nie powinny zwierać logiki biznesowej i powinny wszystkie operacje wykonywać za pomocą usługi w ramach której uruchomiona jest baza danych H2
1. Usługa umożliwiająca dostęp do zasobu `/users` powinna wymagać autoryzacji na poziomie podstawowym [HTTP Basic](https://en.wikipedia.org/wiki/Basic_access_authentication)

## Kryterium oceny rozwiązania
```diff
! Za poprawne rozwiązania zadania można otrzymać 5 punktów.
```
**1. Zgodność oraz poprawność implementacji opisanej w ramach wymagań funkcjonalnych i tych dotyczących architektury**
> Aplikacja powinna umożliwiać:
> * pobranie listy użytkowników, usuwanie oraz dodawanie nowych użytkowników,
> * pobranie listy dostępnych książek,
> * pobranie informacji o książce wraz z jej historią wypożyczeń
> * wypożyczenie oraz zwrot książki przez użytkownika
> * w przypadku braku autoryzacji do zasobów aplikacja powinna zwracać błąd `401 Forbidden`
> * aplikacja powinna składać się z 4 niezależnych procesów
> * kod źródłowy wszystkich procesów powinien znajdować się w ramach jednego repozytorium w oddzielnych katalogach
>
> Dodatkowa funkcjonalność nie wymagana w ramach zadania nie będzie wypływała na ocenę końcową.

**2. Sprawozdanie z laboratorium**
> Dołączenie sprawozdania do zrealizowanego zdania jest warunkiem koniecznym do uzyskania pozytywnej oceny z laboratorium. Zadania bez sprawozdania lub ze sprawozdaniem zawierającym znaczące braki merytoryczne nie będą podlegały ocenie.
>
> Sprawozdanie powinno zostać zamieszczone w katalogu [docs](docs) i dodane do repozytorium w oddzielnym commicie pod tytułem "**Sprawozdanie**".

**3. Termin dostarczenia rozwiązania**
> Bezpośrednio po zajęciach w repozytorium powinny znaleźć się wynik prac zakończonych w trakcie laboratorium. Na podstawie tego commitu zaliczona zostanie obecność na zajęciach.
> 
> Ostatecznym terminem na wysłanie rozwiązania zadania wraz ze sprawozdaniem jest **10.04.2022 23:59** (decyduje data ostatniego commitu). Ocena rozwiązania dostarczonego po tym terminie będzie automatycznie obniżana o 1 punkt.
> 
> Rozwiązania nadesłane po **17.04.2022 23:59** będą miały obniżoną ocenę o 2 punkty, a po **24.04.2022 23:59** nie będą oceniane.

## Zadania do wykonania w ramach laboratorium

### Krok 1
Wykonaj lokalną kopię prywatnego repozytorium z zadaniem dostępnego na platformie GitHub Classroom.

```diff
! W ramach wstępu do sprawozdania wyjaśnij zalety i wady aplikacji opartych o mikroserwisy
! w porównaniu do aplikacji monolitycznych.
```

### Krok 2
Wygeneruj za pomocą [https://start.spring.io](https://start.spring.io) projekt startowy dla języka Java 11 oparty o narzędzie Maven. Wymagania do projektu:
> * Metoda dystrybucji: **JAR**
> * Dane projektu:
>    * Grupa: **pl.edu.pk.ztp**
>    * Artefakt i nazwa: **library-discovery-service**
>    * Opis: **Aplikacja pełniąca funkcję rejestru usług biblioteki**
>    * Nazwa paczki: **pl.edu.pk.ztp.library.discovery**
> * Wersja Spring Boot: **2.6.6**
> * Wymagane zależności:
>    * Eureka Server

Katalog `library-discovery-service` wraz z całą zawartością skopiuj do katalogu głównego repozytorium, a następnie w nowym oknie wybranego IDE otwórz projekt.

### Krok 3
Zaktualizuj konfigurację aplikacji zapisaną w pliku `application.properties` zgodnie z wymaganiami poniżej:
```ini
server.port=8761

eureka.client.register-with-eureka=false
eureka.client.fetch-registry=false

logging.level.com.netflix.eureka=OFF
logging.level.com.netflix.discovery=OFF
```
Uruchom aplikację i zapoznaj się z informacjami dostępnymi pod adresem [http://localhost:8761/](http://localhost:8761/) 

```diff
! W ramach sprawozdania wyjaśnij znaczenie poszczególnych opcji konfiguracyjnych 
! oraz załącz zrzut ekranu przeglądarki z wyjaśnieniem poszczególnych sekcji 
! widocznych pod adresem http://localhost:8761/
```

### Krok 4
Wygeneruj za pomocą [https://start.spring.io](https://start.spring.io) projekt startowy dla języka Java 11 oparty o narzędzie Maven. Wymagania do projektu:
> * Metoda dystrybucji: **JAR**
> * Dane projektu:
>    * Grupa: **pl.edu.pk.ztp**
>    * Artefakt i nazwa: **library-db-service**
>    * Opis: **Aplikacja do obsługi łączności z bazą danych**
>    * Nazwa paczki: **pl.edu.pk.ztp.library.db**
> * Wersja Spring Boot: **2.6.6**
> * Wymagane zależności:
>    * Spring Web
>    * Eureka Discovery Client
>    * Baza danych H2
>    * Moduł Flyway
>    * JDBC API

Katalog `library-db-service` wraz z całą zawartością skopiuj do katalogu głównego repozytorium, a następnie w nowym oknie wybranego IDE otwórz projekt.

### Krok 5
Przenieś cały kod oraz konfigurację projektu zrealizowanego na poprzednich zajęciach do nowoutrzonego projektu w katalogu `library-db-service`.
Zwróć uwagę aby pakiety `dto`, `repository` oraz `rest` znajdowały się wewnątrz `pl.edu.pk.ztp.library.db`. Po przeniesieniu kodu może okazać się konieczne poprawienie "importów" w skopiowanych plikach. 

Zastąp ścieżkę dostępu do zasobów skopiowanych z poprzedniej aplikacji
* Dla `pl.edu.pk.ztp.library.db.rest.UsersController` zmień `@RequestMapping("/users")` na `@RequestMapping("/internal/users")`
* Dla `pl.edu.pk.ztp.library.db.rest.BooksController` zmień `@RequestMapping("/books")` na `@RequestMapping("/internal/books")`

### Krok 6
Do konfiguracji aplikacji z poprzednich zajęć zapisanej w pliku `application.properties` dodaj następujące wartości:
```ini
spring.application.name = library-db-service
server.port=0
```

Do klasy startowej modułu `pl.edu.pk.ztp.library.db.LibraryDbServiceApplication` dodaj adnotację `@EnableDiscoveryClient`.

```diff
! W ramach sprawozdania wyjaśnij znaczenie nowych opcji konfiguracyjnych oraz adnotacji @EnableDiscoveryClient
```

### Krok 7
Wygeneruj za pomocą [https://start.spring.io](https://start.spring.io) projekt startowy dla języka Java 11 oparty o narzędzie Maven. Wymagania do projektu:
> * Metoda dystrybucji: **JAR**
> * Dane projektu:
>    * Grupa: **pl.edu.pk.ztp**
>    * Artefakt i nazwa: **library-users-service**
>    * Opis: **Aplikacja do zarządzania użytkownikami biblioteki**
>    * Nazwa paczki: **pl.edu.pk.ztp.library.users**
> * Wersja Spring Boot: **2.6.6**
> * Wymagane zależności:
>    * Spring Web
>    * Eureka Discovery Client
>    * Spring Security
>    * Spring Reactive Web

Katalog `library-users-service` wraz z całą zawartością skopiuj do katalogu głównego repozytorium, a następnie w nowym oknie wybranego IDE otwórz projekt.

### Krok 9
Do konfiguracji aplikacji `library-users-service` zapisanej w pliku `application.properties` dodaj następujące wartości:
```ini
spring.application.name = library-user-service
server.port=0
```

Do klasy startowej modułu `pl.edu.pk.ztp.library.users.LibraryUsersServiceApplication` dodaj adnotację `@EnableDiscoveryClient`.

### Krok 10
Dodaj do aplikacji `library-users-service` klasę `pl.edu.pk.ztp.library.users.rest.UsersController` odpowiedzialną za obsługę zasobu `/users` zgodnie z dokumentacją zamieszczoną w [docs/library-rest-service.yaml](https://epam-online-courses.github.io/ZTP-Java-REST-Monolith/).
Klasa powinna udostępniać następujące metody publiczne:
* `Mono<String> getAllUsers()`
* `Mono<String> getUserById(final Integer userID)`
* `void deleteUser(final Integer userID)`
* `Mono<String> postUser(final String user)`

### Krok 11
Do klasy `pl.edu.pk.ztp.library.users.rest.UsersController` wstrzyknij klienta rejestru usług `com.netflix.discovery.EurekaClient` i zaimplementuj pobieranie adresu usługi `library-db-service`.
Zaimplementuj metody publiczne zdefiniowane w poprzednim kroku w oparciu o reaktywnego klienta HTTP (`org.springframework.web.reactive.function.client.WebClient`).

```diff
! W ramach sprawozdzania omów poszczególne etapy pobierania adresu usługi oraz sposobu budowania zapytań HTTP w oparciu o klasę WebClient i obsługę błędów.
```

### Krok 12
Dodaj autoryzację do modułu `library-users-service` w oparciu o HTTP Basic. 
* Nazwa użytkownika: **root**
* Hasło użytkownika: **secret**
* Rola użytkownika: **USER**

```diff
! W ramach sprawozdzania szczegółowo udokumentuj poszczególne elementy wykorzystane do konfiguracji procesu autoryzacji aplikacji
```

### Krok 13
Wygeneruj za pomocą [https://start.spring.io](https://start.spring.io) projekt startowy dla języka Java 11 oparty o narzędzie Maven. Wymagania do projektu:
> * Metoda dystrybucji: **JAR**
> * Dane projektu:
>    * Grupa: **pl.edu.pk.ztp**
>    * Artefakt i nazwa: **library-books-service**
>    * Opis: **Aplikacja do obsługi procesu wypożyczania**
>    * Nazwa paczki: **pl.edu.pk.ztp.library.books**
> * Wersja Spring Boot: **2.6.6**
> * Wymagane zależności:
>    * Spring Web
>    * Eureka Discovery Client
>    * Spring Reactive Web

Katalog `library-books-service` wraz z całą zawartością skopiuj do katalogu głównego repozytorium, a następnie w nowym oknie wybranego IDE otwórz projekt.

### Krok 14
Do konfiguracji aplikacji `library-books-service` zapisanej w pliku `application.properties` dodaj następujące wartości:
```ini
spring.application.name = library-books-service
server.port=0
```

Do klasy startowej modułu `pl.edu.pk.ztp.library.books.LibraryBooksServiceApplication` dodaj adnotację `@EnableDiscoveryClient`.

### Krok 15
Dodaj do aplikacji `library-books-service` klasę `pl.edu.pk.ztp.library.books.rest.BooksController` odpowiedzialną za obsługę zasobu `/books` zgodnie z dokumentacją zamieszczoną w [docs/library-rest-service.yaml](https://epam-online-courses.github.io/ZTP-Java-REST-Monolith/).
Klasa powinna udostępniać następujące metody publiczne:
* `Mono<String> getAllBooks(boolean showOnlyAvailable)`
* `Mono<String> getBookRentals(Integer bookID)`
* `Mono<String> patchReturnBook(Integer bookID, Integer userID)`
* `Mono<String> patchRentBook(Integer bookID, Integer userID)`

### Krok 16
Do klasy `pl.edu.pk.ztp.library.books.rest.BooksController` wstrzyknij klienta rejestru usług `com.netflix.discovery.EurekaClient` i zaimplementuj pobieranie adresu usługi `library-db-service`.
Zaimplementuj metody publiczne zdefiniowane w poprzednim kroku w oparciu o reaktywnego klienta HTTP (`org.springframework.web.reactive.function.client.WebClient`).

```diff
! W ramach sprawozdzania elementy WebClient API które nie zostały omówione w ramach punktu 11.
! Zaznacz w sprawodzaniu zalety oraz typowe przypadki użycia dla programowania reaktywnego.
```

### Krok 17
Przetestuj poprawność działania aplikacji za pomocą narzędzia Postman lub dowolnego innego narzędzia.
* Przykładowe pliki testów dla zasobu `/users` znajdują się w pliku [docs/postman_test_users.json](docs/postman_test_users.json)
* Przykładowe pliki testów dla zasobu `/books` znajdują się w pliku [docs/postman_test_books.json](docs/postman_test_books.json)
```diff
! Wyniki testów dla następujących metod wraz z omówieniem dołącz do sprawozdania.
! -- GET /users (uwzględniając obsługę błędów)
! -- DELETE /users (uwzględniając obsługę błędów)
! -- POST /users
! -- GET /books (uwzględniając filtrowanie)
! -- PATCH /books/return lub PATCH /books/rent (uwzględniając obsługę błędów)
```




