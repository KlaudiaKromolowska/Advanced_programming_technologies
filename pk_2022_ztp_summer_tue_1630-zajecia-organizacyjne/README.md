# PK_2021_ZTP_Zajecia_Organizacyjne


1.  Utwórz konto na [GitHub](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home)'ie.
2.  Zainstaluj GIT'a zgodnie z instrukcją na stronie [Pierwsze kroki - Instalacja Git](https://git-scm.com/book/pl/v2/Pierwsze-kroki-Instalacja-Git)

#### Poniższa procedura będzie się powtarzała na kolejnych zajęciach.

### Inicjalizacjia repozytorium z zadniem.

1.  Od prowadzącego zajecia otrzymasz zaproszenie lub link do GitHub Classroom'u w którym znajdować się będzie zadanie do wykonania. 
2.  Otwórz link i zaakceptuj zaproszenie. GitHub Classroom utworzy na Twoim koncie GitHub repozytorium dedytkowane do danych zajęć.
3.  Gdy repozytorium zostanie utworzone, przejdź do nowo utworzonego repozytorium i przeczytaj instrukcje (najczęściej będzie to plik README.md który zobaczymy po otwarciu linku)
4.  Zauważ, że zostały utworzone dwie gałęzie (branch'e) `main` oraz `feedback`. 

*** ZAPAMIĘTAJ *** 
PRACUJEMY NA GAŁĘZI `main`

Jeśli chcesz zakomitować zmiany zrób to na gałęzi `main`

5. W zakładce Pull requests został również utworzony specjalny pull request `Feedback`. Pull request jest funcjonalnością która pozwala wykonać przegląd kodu (zmian), komentować a następnie akceptować lub odrzucić zmiany któr programista chce dodać do centralnego repozytorium.

Często posugujemy się skrótem PR = **P**ull **R**equests.


### Praca na lokalnym repozytorium.

1. Na lokalnym komputerze utwórz katalog w którym będziesz przechowywał repozytoria do zajęć np. ztp-repositoies
2. Przejdź to utworzonego katalogu i sklonuj repozytorium z GITHub'a
  >`git clone <http-url>`
  gdzie `<http-url>` jest adressem do repozytorium na GITHub'ie. Link znajduje się pod zielonym przyciskiem o nazwie `<code>`.

3. Link do repozytrotium na GitHub'a znajduje się pod przyciskiem `<code>` na stronie naszego repozytorium. 
4. Git utworzył katalog o nazwie jaką ma repozytorium na GitHubie.
5. Przejdź do katalogu i przełącz się na gałąź `main`:
   > `git checkout main`

6. Pracuj nad rozwiazaniem zadania. 

### Rejestracja zmian w lokalnym repozytorium

Zalecane jest aby wykoywać commity gdy mamy pewną część gotowego rozwiązania np. zainicjalizowane środowisko developerskie lub gdy jakaś część kodu jest napisana (nie koniecznie jeszcze działająca poprawnie). Takie podejście pozwala nam w łatwy sposób cofnąć zmiany i wrócić do właściwej wersji kodu. Jak również w pewnym sensie dokumentujemy nasza pracę.
Aby wykonać commit (zarejestrować bieżące zmiany) wykonujemy następujace kroki:
  - dodać zmiany które chcemy zakomitować do tzw. 'poczekalni':
     >`git add .`
 
  lub jeśli chcemy zakomitować zmiany tylko w wybranych plikach lub folderach:
  
   >`git add plik1.py plik2.py folderA folderB`
 
  - rejestracja zamiany w repozytorium (wykonanie commita)
    >`git commit -m <message>`

gdzie <message> - jest komentarzem który musimy dodać do commita. Najczęściej podajemy co zostało zmiennione, dodane.

### Wypychanie zmian do GitHub'a.
Jeśli chcemy udostępnić kod na GITHubie, np. chcemy skonsultować dotychczasową pracę z prowadzącym, lub chcemy wysłać zadanie do oceny należy 'wypchnąć' zmiany do centralnego repozytorium. Wykonaj następujace kroki:
  1. Sprawdź czy wszystkie zmiany które chcesz udostępnić zostały zarejstrowane w lokalnym repozytorium.
  2. Jeśli pracowałeś na innej gałęzi niż `main` scal zmiany z bieżącej gałęzi do gałęzi `main` - użyj komnedy [`git merge`](https://git-scm.com/book/pl/v2/Ga%C5%82%C4%99zie-Gita-Podstawy-rozga%C5%82%C4%99ziania-i-scalania)
  
  :bangbang: UWAGA :bangbang:
  ** NIE UŻYWAJ GAŁĘZI `feedback` DO PRACY JEST ONA ZAREZERWOWANA DO SCALANIA ZMIAN z GAŁĘZI `main` NA GITHUBIE **
  
  3. Aby wypchać zmiany do centralnego repozytorium użyj polecenia:
  
    >`git push`
  
  4. Przejdź do zakładki `Pull requests` na GitHub'e a nastepnie otwórz `feedback` - Twoje zmiany powinny być widoczne.
  5. Jeśli jest taka potrzeba dodaj komentarz.
  6. Aby prowadzący mógł przeglądnąć Twój kod, lub ocenić dodaj go do listy w polu `Reviewers` po lewej stronie.
  7. Możesz również na MS Teamsach poinformować prowadzącego aby przeglądną Twój kod.
  
  :bangbang: UWAGA :bangbang:
  ** NIE ZAMYKAJ  `Pull requests feedback` JAK RÓWNIEŻ NIE SCALAJ ZMIAN W TYM  PULL REQUESTS'cie **
  
  
### Zadanie
  1. Sklonuj bieżące repozytorium na komputer lokalny.
  2. W katalogu głównym utwórz plik zajecia_organizacyjne.txt
  3. Zarejestruj zmiany w repozytorium lokalnym - dodając komentarz - "Utworzono plik zajec organizacyjnych".
  4. Wyeksportuj bieżące zmiany do repozytorium centralnego.
  5. Dodaj komentarz w PR `Feedback` o treści "Plik zajęcia organizacyjne został utworzony"
  6. Dodaj prowadzącego jako `Reviewers`
  
  7. Lokalnie dodaj tekst "Czy to jest poprwne" do pliku zajecia_organizacyjne.txt
  8. Zarejestruj zmiany lokalnie i wypchaj je na GitHub'a.
  
  9. Skomentuj dodaną linie tekstu w pliku zajecia_organizacyjne.txt w PR Feedback na GitHubie.
