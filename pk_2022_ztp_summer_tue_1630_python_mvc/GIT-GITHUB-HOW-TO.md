## Praca z git'em oraz GitHub'em.

<br />
<br />

### `main` jest głównym branch'em na którym pracuje student.

### `feedback` jest branch'em na który **NIE ZAPISUJEMY JAKICHKOLWIEK ZMIAN !!!**. Ten branch pozostaje "czysty".
<br />
<br />

### Praca na lokalnym repozytorium.

1. Jeśli mamy potrzebę utworzenia kolejnych branch'ów to możemy jak najbardziej to zrobić pamiętając że branch'em wyjściowym powinien być `main` lub pochodny od niego.
   
2. Kod programu który chcemy wysłać do oceny musi znajdować się na branch'u `main`. Stąd jeśli zapisywaliśmy zmiany na innym branch'u niż `main` wówczas scalamy zmiany do branch'a `main`.


3. Przed wysłaniem wersji finalnej naszej aplikacji na GitHub'a jeśli prowadzący zajęcia udostępnił nam testy jednostkowe to uruchommy te testy  i sprawdźmy czy jeszcze jesteśmy w stanie coś poprawić w naszym kodzie, oraz czy wynik jest dla nas satysfakcjonujący.

### Praca z GitHub'em.

1. Po wypchnięciu zmian na GitHub'a nie twórzmy 'Pull requestów' (*dalej PR*). Class room utworzył już PR `Feedback` na którym możemy pozostawić komentarz do kodu, jak również tutaj będą komentarze od prowadzącego. Jeśli widzimy że nasze zmiany są w GitHub'ie na gałęzi `main` dodaj ewentualnie komentarz i to wszystko.
   
2. **W ŻADNYM WYPADKU NIE ZAMYKAJMY PULL REQUESTS `Feedback` !!!**

3. Dodawanie komentarza do pull request `Feedback`.
	
    * przejdź do zakładki `Pull requests`,
	* kliknij na otwarty PR o nazwie `Feedback`,
	* przejdź do zakładki `Conversation`,
	* Na dole strony znajduje się okno w którym możemy dodać komentarz,
	* Aby przesłać komentarz kliknij w przycisk `Comment`,
	* **NIE KLIKAJ W PRZYCISK `Close pull request` lub `Merge pull request`**
  
4. Dodawanie komentarza pytania do wybranej lini kodu:
	* przejdź do zakładki `Files changed`, zobaczysz listę ze zmianami jakie dokonałeś w poszczególnych plikach.
	* wybierz plik w którym chcesz pozostawić komentarz,
	* najedź kursorem na linie kodu do której chcesz dodać komentarz, po lewej stronie zostanie wyświetlona ikona `+`,
	* kliknij w ikonę `+` - otworzy się okno komentarza,
	* pozostaw swój komentarz, pytanie,
	* zapisz komentarza - kliknij w `Add single comment`
