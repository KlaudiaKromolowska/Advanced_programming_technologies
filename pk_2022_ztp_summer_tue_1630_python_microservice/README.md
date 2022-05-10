[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7620195&assignment_repo_type=AssignmentRepo)
## 1. Temat zadania
___
Zaimplementuj dwa mikroserwisy, które pozwolą odseparować realizację usług administracyjnych biblioteki takich jak zarządzanie użytkownikami oraz tytułami książek od usług związanych z wypożyczaniem książek takich jak przeszukiwanie katalogu tytułów, wypożyczanie i zwroty egzemplarzy tytułów.
___

## 2. Definicja enpoint`ów dla API:
### - library_microservice:
 
  1. Pobieranie listy użytkowników:
     >  GET /users
      
  2. Pobieranie szczegółowych informacji o koncie użytkownika dla podanego `id`:
      > GET /users/<<id: integer>>
  
  3. Liczba wypożyczonych książek przez użytkownika o podanym `id`:
      > GET /users/<<id: integer>>/books

  4. Pobieranie lista tytułów książek z bazy biblioteki:
      > GET /books

  4. Obsługa wypożyczenia egzemplarza tytułu książki o podanym `id`:
      > PATCH /books/rent/<<id: integer>> 

    
### - admin_microservice:

  1. Dodawanie nowego użytkonika do systemu:
      > POST /api/users
      
  2. Pobieranie listy użytkowników:
      > GET /users

  3. Pobieranie informacji o użytkowniku dla podanego `id`:
      > GET /users/<<id: integer>>


      
## 3. Konfiguracja środowiska developerskiego.
1. Przejdź do katalogu w którym przechowujesz repozytoria do przedmiotu ZTP. Jeśli jeszcze takiego nie posiadasz utwórz nowy katalog np. o nazwie `lab-ztp`.
2. Do katalogu `lab-ztp` sklonuj repozytorium  `pk_ztp_lab_02_python_microservices-<<username>>`:
   
    > `git clone pk_ztp_lab_01_python_rest-<<username>>`

3. Przejdź do folderu zawierajacego sklonowane repozytorium.
4. Utwórz wirtualne środowisko python:
    > `python3 -m venv .venv`

5. Aktywuj wirtualne środowisko:
    > `.ven\Scripts\activate`

6. Zainstaluj framework Flask:
   > `pip install flask`

7. Przejdź do katalogu `src\` i utwórz dwa pliki `library_microservice.py` oraz `admin_microservice.py`
  
8. Upewnij się, że pracujesz na gałęzi `main`:
    > `git status`
  
    jeśli nie, przełącz się na gałąź `main`:

    > `git checkout main`

9.  Dodaj katalog .venv to pliku .gitignore.

10. Utwórz migawkę kodu do repozytorium:
    > `git add .`\
    > `git commit -m "Konfiguracja środowiska developerskiego"`

11. Rozpocznij pisanie kodu dla poszczeglnych mikroserwisw.


## 4. Logika dla poszczególnych mikroserwisów.
### - admin_microservice
Serwis jest odpowiedzialny za zarządzanie użytkownikami w naszej organizacji.
Powinnien mieć zaimplementowaną logikę:
  - dodawanie nowego użytkownika do organizacji,
  - podczas tworzenia nowego użytkonika powinna być możliwość oznaczenia czy użytkonik ma dostęp do biblioteki,
  - usuwanie użytkonika z organizacji, przy czym nie można usunąć użytkownika jeśli posiada wypożyczone książki,
  
### - library_microservice
Serwis odpowiedzialny za obsługę biblioteki. Powinien mieć zaimplementowaną następującą logikę:
- pobieranie listy tytułów książek,
- obsługę wypożyczania danego tytułu,
- pobieranie listy użytkoników,
- pobranie informacji o stanie konta dla użytkownika o podanym id.
    
  
