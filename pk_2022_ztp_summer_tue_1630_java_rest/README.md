# L03: Zaawansowane techniki programowania

Celem zadania będzie przygotowanie monolitycznej aplikacji udostępniającej prosty interfejs REST w oparciu Spring Boot i język Java.

## Przygotowanie

Przed zajęciami proszę o zapoznanie się z [załączonymi materiałami](docs/introduction.md) oraz o zainstalowanie niezbędnego oprogramowania, które będzie wykorzystywane na tych i kolejnych zajęciach.
W przypadku braku znajomości języka SQL polecam zapoznanie się z [dodatkowymi materiałami pomocniczymi](docs/sql_cheetsheet.md) wymaganymi do realizacji komunikacji z bazą danych.

## Wymagania dotyczące aplikacji

1. Dostęp do aplikacji nie powinien wymagać autoryzacji, a po uruchomieniu aplikacji wszystkie zasoby powinny być dostępne pod adresem [http://localhost:8080](http://localhost:8080).
1. Zasoby i funkcjonalność powinny być udostępniane przez REST API zgodne z dokumentacją zawartą w [docs/library-rest-service.yaml](https://epam-online-courses.github.io/ZTP-Java-REST-Monolith/).
1. Aplikacja powinna wykorzystywać wbudowaną bazę danych H2 do przechowywania stanu systemu.

## Kryterium oceny rozwiązania
```diff
! Za poprawne rozwiązania zadania można otrzymać 5 punktów.
```
**1. Zgodność oraz poprawność implementacji funkcjonalności opisanej w ramach REST API**
> Aplikacja powinna umożliwiać:
> * pobranie listy użytkowników, usuwanie oraz dodawanie nowych użytkowników,
> * pobranie listy dostępnych książek,
> * pobranie informacji o książce wraz z jej historią wypożyczeń
> * wypożyczenie oraz zwrot książki przez użytkownika
>
> Proszę zwrócić szczególną uwagę na trzymanie się formatu danych (JSON) oraz obsługi błędów zdefiniowanych w ramach dokumentacji [REST API](https://epam-online-courses.github.io/ZTP-Java-REST-Monolith/).
> Dodatkowa funkcjonalność nie wymagana w ramach zadania nie będzie wypływała na ocenę końcową.

**2. Sprawozdanie z laboratorium**
> Dołączenie sprawozdania do zrealizowanego zdania jest warunkiem koniecznym do uzyskania pozytywnej oceny z laboratorium. Zadania bez sprawozdania lub ze sprawozdaniem zawierającym znaczące braki merytoryczne nie będą podlegały ocenie.
>
> Sprawozdanie powinno zostać zamieszczone w katalogu [docs](docs) i dodane do repozytorium w oddzielnym commicie pod tytułem "**Sprawozdanie**".

**3. Termin dostarczenia rozwiązania**
> Bezpośrednio po zajęciach w repozytorium powinny znaleźć się wynik prac zakończonych w trakcie laboratorium. **Na podstawie tego commitu zaliczona zostanie obecność na zajęciach.** 
>
> Ostatecznym terminem na wysłanie rozwiązania zadania wraz ze sprawozdaniem jest **03.04.2022 23:59** (decyduje data ostatniego commitu).
> Ocena rozwiązania dostarczonego po tym terminie będzie automatycznie obniżana o 1 punkt. 
> 
> Rozwiązania nadesłane po **10.04.2022 23:59** będą miały obniżoną ocenę o 2 punkty, a po **17.04.2022 23:59** nie będą oceniane. 

```diff
! Punkty za rozwiązanie zostaną przyznane tylko w przypadku gdy do rozwiązania dołączone 
! będzie sprawozdanie zawierające wszystkie wymagane elementy. 
```

## Zadania do wykonania w ramach laboratorium

### Krok 1
Wykonaj lokalną kopię prywatnego repozytorium z zadaniem dostępnego na platformie GitHub Classroom.

### Krok 2
Wygeneruj za pomocą [https://start.spring.io](https://start.spring.io) projekt startowy dla języka Java 11 oparty o narzędzie Maven. Wymagania do projektu:
> * Metoda dystrybucji: **JAR**
> * Dane projektu:
>    * Grupa: **pl.edu.pk.ztp**
>    * Artefakt i nazwa: **library-monolith**
>    * Opis: **Aplikacja typu monolit do obsługi biblioteki**
>    * Nazwa paczki: **pl.edu.pk.ztp.library-monolith**
> * Wersja Spring Boot: **2.6.4**
> * Wymagane zależności:
>    * Spring Web
>    * Baza danych H2
>    * Moduł Flyway
>    * JDBC API

### Krok 3
Pobrany szablon projektu rozpakuj do katalogu głównego repozytorium tak, aby katalog `src` z archiwum znajdował się w bezpośrednio w katalogu głównym repozytorium.
```diff
! Wykonaj zrzut ekranu struktury projektu po zaimportowaniu do IDE i dołącz do sprawozdania.
```
### Krok 4
Zaktualizuj konfigurację projektu w IDE tak, aby był on rozpoznawany jako projekt Mavenowy, a następnie uruchom aplikację.
```diff
! Wynik uruchomienia dołącz do sprawozdania wraz z komentarzem wyjaśniającym 
! poszczególne etapy inicjalizacji aplikacji oraz źródło błędu.
```
### Krok 5
Zaktualizuj konfigurację połączenia do bazy danych H2 zapisaną w pliku `application.properties` zgodnie z wymaganiami poniżej:
```ini
   spring.datasource.url=jdbc:h2:mem:librarydb
   spring.datasource.driverClassName=org.h2.Driver
   spring.datasource.username=admin
   spring.datasource.password=password
   spring.h2.console.enabled=true
```
```diff
! W ramach sprawozdania wyjaśnij znaczenie poszczególnych opcji konfiguracyjnych.
```
### Krok 6
Przenieś plik odpowiedzialny za inicjalizację bazy danych `V1_0__create_librarydb_schema.sql` z katalogu [docs](src/main/resources/db/migration/V1_0__create_librarydb_schema.sql) do `resources/db/migration` oraz uruchom aplikację ponownie.
```diff
! Wynik uruchomienia dołącz do sprawozdania wraz z komentarzem 
! wyjaśniającym poszczególne etapy inicjalizacji aplikacji.
```
### Krok 7
Dodaj do aplikacji klasy odpowiedzialne za reprezentacje danych w formacie JSON zgodnie z dokumentacją zamieszczoną w [docs/library-rest-service.yaml](https://epam-online-courses.github.io/ZTP-Java-REST-Monolith/).
* `pl.edu.pk.ztp.librarymonolith.dto.UserDTO` reprezentacja modelu **User**
* `pl.edu.pk.ztp.librarymonolith.dto.BookDTO` reprezentacja modelu **Book**
* `pl.edu.pk.ztp.librarymonolith.dto.BookRentalDTO` reprezentacja modelu **BookRental**
```diff
! W ramach sprawozdania wyjaśnij kluczowe adnotacje wykorzystane 
! do konfiguracji procesu serializacji do formatu JSON.
```
### Krok 8
Dodaj do aplikacji klasę repozytorium odpowiedzialną za udostępnianie danych zapisanych w bazie danych w tabeli `tbl_users`. 
Klasa powinna posiadać następującą nazwę `pl.edu.pk.ztp.librarymonolith.repository.UserRepository` oraz udostępniać następujące metody publiczne:
* `List<UserDTO> findAll()`
* `UserDTO findByUserId(final Integer userID)`
* `boolean deleteUserById(final Integer userID)`
* `UserDTO createUser(final UserDTO user)`
```diff
! W ramach sprawozdania wyjaśnij cel oraz działanie zastosowanych 
! w ramach tej klasy adnotacji @Repository oraz @Autowired
```
### Krok 9
Dodaj do aplikacji klasę `pl.edu.pk.ztp.librarymonolith.rest.UsersController` odpowiedzialną za obsługę zasobu `/users` zgodnie z dokumentacją zamieszczoną w [docs/library-rest-service.yaml](https://epam-online-courses.github.io/ZTP-Java-REST-Monolith/).
Klasa powinna udostępniać następujące metody publiczne:
* `List<UserDTO> getAllUsers()`
* `UserDTO getUserById(final Integer userID)`
* `void deleteUser(final Integer userID)`
* `UserDTO postUser(final UserDTO user)`
```diff
! W ramach sprawozdania wyjaśnij kluczowe elementy wykorzystane do konfiguracji zasobu 
! zgodnie z dokumentacją oraz sposób w jaki rozwiązana została obsługa błędów.
```
### Krok 10
Dodaj do aplikacji klasę repozytorium odpowiedzialną za udostępnianie danych zapisanych w bazie danych w tabeli `tbl_books` oraz `tbl_rentals`. Klasa powinna posiadać następującą nazwę `pl.edu.pk.ztp.librarymonolith.repository.BookRepository`
```diff
! W ramach sprawozdania udokumentuj publiczne metody zdefiniowane w ramach tej klasy.
! Opis powinien zawierać sygnaturę metody oraz krótki opis jej działania.
``` 
### Krok 11
Dodaj do aplikacji klasę `pl.edu.pk.ztp.librarymonolith.rest.BooksController` odpowiedzialną za obsługę zasobu `/books` zgodnie z dokumentacją zamieszczoną w  [docs/library-rest-service.yaml](https://epam-online-courses.github.io/ZTP-Java-REST-Monolith/).
Klasa powinna udostępniać następujące metody publiczne:
* `List<BookDTO> getAllBooks(final boolean showOnlyAvailable)`
* `BookDTO getBookRentals(final Integer bookID)`
* `BookDTO patchRentBook(final Integer bookID, final Integer userID)`
* `BookDTO patchReturnBook(final Integer bookID, final Integer userID)`
```diff
! W ramach sprawozdania wyjaśnij kluczowe elementy wykorzystane do konfiguracji zasobu 
! zgodnie z dokumentacją oraz sposób w jaki rozwiązana została obsługa błędów.
```
### Krok 12
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




