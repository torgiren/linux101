% Wprowadzenie do systemu GNU/Linux
% Marcin Fabrykowski
% ![](img/logo.png){heigth=50px} ![](img/akamai-logo.png){heigth=50px}

## Prezentacja

::: nonincremental

- dostępna pod adresem:  
  https://torgiren.github.io/linux101

- repozytorium:  
  https://github.com/torgiren/linux101

:::

## Czym jest system operacyjny?

- To program, który zarządza zasobami komputera.

- Zapewnia warstwę abstrakcji pomiędzy sprzętem a programami użytkownika.

- Pozwala na uruchamianie innych programów.

## Architektura

![](img/systemstructure.png)

## Jak wygląda OS? {data-transition="none-out"}

Windows

![](img/os_windows1.png){width=85%}

## Jak wygląda OS? {data-transition="none"}

Linux

![](img/os_linux1.png)

## Jak wygląda OS? {data-transition="none"}

Linux

![](img/os_linux2.png){width=80%}

## Jak wygląda OS? {data-transition="none slide-out"}

Linux

![](img/os_linux3.gif){width=80%}

## Po co mi Linux?

- Po prostu desktop
- Administracja serwerami
- Programowanie (kontenery)
- Raspberry Pi

## Dlaczego Linux? {data-transition="none-out"}

- Otwartość kodu źródłowego

- Darmowość

- Bezpieczeństwo

- Stabilność

- Konfigurowalność

- Zasobożerność (a raczej jej brak)

::: notes

goły system ok 70 MB RAM.
z httpd i mysql ok 150 MB RAM

:::


## Plan warsztatów

::: nonincremental

- łączenie się z serwerem
- konfiguracja strony WWW
- bazując na otrzymanym efekcie, zrozumienie podstawowych operacji na systemie, czyli:
  - poruszanie się po systemie
  - operacje na plikach i katalogach
- obsługa edytora vim
- podstawy wyrażeń regularnych
- konfiguracja bloga opartego o Wordpress

:::

## Konwencje w prezentacji

- `polecenie` - polecenie, które należy wpisać w terminalu
- `<nazwa>` - zmienna, którą należy zastąpić odpowiednią wartością (bez znaków `<` i `>`)
- `cd <userX>` == `cd user40` (dla `user40`)

## łączenie się z serwerem

- Ściągnij program PuTTY (https://putty.org/)
- Wpisz adres: `ssh.warsztaty.linux.org.pl`
- Wpisz login: `<userX>` (np. `user40`)
- Wpisz hasło: `<userX>_pass` (np: `user40_pass`; hasło nie będzie wyświetlane)
- Już :)

## Prompt

~~~~~~~
user3@warsztaty:~$
~~~~~~~
- `user3` - nazwa użytkownika
- `@` - at
- `warsztaty` - nazwa hosta
- `~` - bieżący katalog
- `$` - zwykły użytkownik
- `#` - administrator

## Składnia poleceń

- `polecenie [opcje] [argumenty]`
- `ls -l /etc`

## konfiguracja strony WWW

~~~~~~~ {.numberLines}
cd /var/www/html/<userX>
cp /var/www/html/user0/v2/strona.tar.gz ./
tar -xzf strona.tar.gz
~~~~~~~ 

np:

~~~~~~~ {.numberLines}
cd /var/www/html/user40
cp /var/www/html/user0/v2/strona.tar.gz ./
tar -xzf strona.tar.gz
~~~~~~~

http://&lt;userX&gt;.warsztaty.linux.org.pl/strona/

## Struktura systemu plików

```
/
├── run
│   ├── agetty.reload
│   ├── apache2
│   │   └── apache2.pid
│   ├── console-setup
│   │   └── boot_completed
├── etc
│   ├── aliases
│   ├── alternatives
│   │   └── aclocal -> /usr/bin/aclocal-1.16
```
- system plików jest drzewem
- `/` - katalog główny
- wszystkie katalogi są podkatalogami katalogu `/`

## Struktura systemu plików

Przykładowe ścieżki do plików i katalogów
```
# katalogi
/etc/
/home/
/home/user1/

# pliki
/etc/passwd
/var/www/html/user1/strona/index.html
/home/user1/strona/index.html
/home/user1/strona/assets/images/show-event-02.jpg
```

## Ścieżki do plików i katalogów

- ścieżki mogą być względne i bezwzględne
- ścieżka względna wskazuje na plik lub katalog względem bieżącego katalogu
- ścieżka bezwzględna wskazuje na plik lub katalog względem katalogu głównego


## Ścieżki do plików i katalogów

Będąc w katalogu  
  `/home/user1/`  
  ścieżka do pliku `index.html` to:

:::::::::::::: {.columns}
::: {.column width="50%"}
- ścieżka względna:  
  ```
  index.html
  ```
- ścieżka bezwzględna:  
  ```
  /home/user1/index.html
  ```
:::
::: {.column width="50%"}
```
home/
├── user1 <==
│   └── index.html
└── user2
    └── notatki.txt
```
:::
::::::::::::::
## Ścieżki do plików i katalogów

Natomiast będąc w katalogu  
  `/home/user2/`  
  ścieżka do tego samego pliku `index.html` to:

:::::::::::::: {.columns}
::: {.column width="50%"}
- ścieżka względna:  
  ```
  ../user1/index.html
  ```
- ścieżka bezwzględna:  
  ```
  /home/user1/index.html
  ```
:::
::: {.column width="50%"}
```
home/
├── user1
│   └── index.html
└── user2 <==
    └── notatki.txt
```
:::
::::::::::::::

## Poruszanie się po systemie

- `pwd` - wyświetla ścieżkę do bieżącego katalogu
- `ls` - wyświetla zawartość katalogu
- `cd <katalog>` - zmienia bieżący katalog
- `mkdir` - tworzy katalog
- `rmdir` - usuwa katalog
- `tree` - wyświetla strukturę katalogów


## najważniejsze katalogi

::: nonincremental

- `/` - katalog główny
- `/etc` - konfiguracja systemu
- `/bin`, `/sbin` - programy systemowe
- `/usr` - programy użytkowe
- `/home` - katalogi użytkowników
- `/tmp` - dane tymczasowe
- `.` - bieżący katalog
- `..` - katalog nadrzędny

:::

## Zadanie 1 - przejście do katalogu ze stroną WWW

::: nonincremental

- stronę WWW umieściliśmy w katalogu:
  ```
  /var/www/html/<userX>/strona
  ```
- przejdź do katalogu ze stroną WWW
- wypisz aktualną ścieżkę
- wyświetl zawartość katalogu

:::

## Zadanie 1 - przejście do katalogu ze stroną WWW

::: nonincremental

- stronę WWW umieściliśmy w katalogu:
  ```
  /var/www/html/<userX>/strona
  ```
- przejście do katalogu ze stroną WWW:
  ```
  cd /var/www/html/<userX>/strona
  ```
- wypisanie aktualnej ścieżki:
  ```
  pwd
  ```
- wyświetlenie zawartości katalogu:
  ```
  ls
  ```

:::

## Operacje na plikach i katalogach

- `cat` - wyświetla zawartość pliku
- `less` - wyświetla zawartość pliku (po stronach)
- `head` - wyświetla początkowe linie pliku
- `tail` - wyświetla końcowe linie pliku
- `cp` - kopiowanie plików
- `mv` - przenoszenie i zmiana nazwy plików
- `rm` - usuwanie plików

## Operacje na plikach i katalogach

- `cat` (bez argumentów) - wyświetla na ekranie dane z wejścia standardowego   
  (ctrl+d lub ctrl+c aby zakończyć)
- `cat <plik>` - wyświetla zawartość pliku
- `tail <plik>` - wyświetla końcowe linie pliku
- `tail -n <liczba> <plik>` - wyświetla ostatnie `<liczba>` linii pliku
- `tail -F <plik>` - wyświetla końcowe linie pliku i śledzi zmiany (ctrl+c aby zakończyć)

## Operacje na plikach i katalogach

- `cp <plik1> <plik2>` - kopiuje plik1 do pliku2
- `cp <plik1> <katalog>` - kopiuje plik1 do katalogu
- `mv <plik1> <plik2>` - zmienia nazwę pliku1 na plik2
- `mv <plik1> <katalog>` - przenosi plik1 do katalogu

## Zadanie 2a - przeglądanie logów serwera WWW

::: nonincremental

- logi serwera WWW znajdują się w katalogu:  
  ```
  /var/log/apache2
  ```
- plik z logami serwera WWW:  
  ```
  /var/log/apache2/<userX>_access.log
  ```
- przejdź do katalogu z logami
- wyświetl zawartość pliku `<userX>_access.log`

:::

## Zadanie 2a - przeglądanie logów serwera WWW

::: nonincremental

- przejdź do katalogu z logami
  ```
  cd /var/log/apache2
  ```
- wyświetl zawartość pliku `<userX>_access.log`
  ```
  cat <userX>_access.log
  ```

:::

## Zadananie 2b - przeglądanie logów serwera WWW

::: nonincremental

- wyświetl 5 ostatnich linii pliku logów:  
- wyświetlaj nowe linie pliku access.log:  
- znajdź linie z kodem 404

:::

## Zadanie 2b - przeglądanie logów serwera WWW

::: nonincremental

- wyświetl 5 ostatnich linii pliku logów:  
  ```
  tail -n 5 <userX>_access.log
  ```
- wyświetlaj nowe linie pliku access.log:  
  ```
  tail -F <userX>_access.log
  ```
- znajdź linie z kodem 404, np:
  ```
  31.179.32.96 - - [18/Oct/2023:17:57:06 +0000] "GET /strona/assets/images/show-events-02.jgp HTTP/1.1" 404 506 "http://user4.warsztaty.linux.org.pl/strona/" "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0"
  ```

:::

## Zadanie 3 - poprawienie brakującego obrazka

::: nonincremental

- na stronie głównej brakuje obrazka
- przejdź do katalogu z brakującym plikiem
- wylistuj pliki w tym katologu
- zmień nazwę pliku z rozszerzeniem .jgp na .jpg
- sprawdź, czy obrazek się wyświetla

:::

## Zadanie 3 - poprawienie brakującego obrazka

::: nonincremental

- przejdź do katalogu z brakującym plikiem
  ```
  cd /var/www/html/<login>/strona/assets/images
  ```
- wylistuj pliki w tym katologu
  ```
  ls
  ```
- zmień nazwę pliku z rozszerzeniem .jgp na .jpg
  ```
  mv show-events-02.jgp show-events-02.jpg
  ```

:::

## Obsługa edytora vim {data-transition="none-out"}

- vim jest edytorem modalnym, czyli ma kilka trybów pracy, m.in.:  
  - tryb normalny
  - tryb wstawiania

## Obsługa edytora vim {data-transition="none"}

- tryb normalny - służy do nawigacji po pliku i wykonywania poleceń
- nawigować można za pomocą klawiszy `h`, `j`, `k`, `l` lub strzałek
- przejście do trybu wstawiania: `i`...
- ...jak również na kilkanaście innych sposobów
- wyjście z trybu wstawiania: `ESC`

## Obsługa edytora vim {data-transition="none"}

- szukanie tekstu: `/tekst`
- zapisanie pliku: `:w`
- wyjście z vim-a: `:q`
- zapisanie i wyjście z vim-a: `:wq`

## Obsługa edytora vim {data-transition="none"}

- kopiowanie i wklejanie tekstu:
  - `yy` - kopiowanie linii
  - `p` - wklejanie
- usuwanie tekstu:
  - `dd` - usuwanie linii
  - `x` - usuwanie znaku
- cofanie i ponawianie zmian:
  - `u` - cofanie
  - `CTRL+r` - ponawianie

## Obsługa edytora vim (extra) {data-transition="none-in"}

- wejście do trybu wstawiania:
  - przed kursorem: `i`
  - za kursorem: `a`
  - na początku linii: `I`
  - na końcu linii: `A`
  - linijka poniżej: `o`
  - linijka powyżej: `O`


## Zadanie 4 - poprawienie linku do strony about us

::: nonincremental
- spróbuj otworzyć stronę `About Us`
- otwórz plik index.html w edytorze vim
- znajdź link do strony `About Us`
- popraw literówkę w linku
- zapisz i sprawdź efekt w przeglądarce
- wyjdź z vim-a
:::

## Zadanie 4 - poprawienie linku do strony about us

::: nonincremental

- znajdź link do strony `About Us`:  
  `/About Us`
- przejdź do trybu wstawiania: `i`
- popraw link
- wyjdź z trybu wstawiania: `ESC`
- zapisz: `:w`
- wyjdź z vim-a: `:q`

:::

## Grep i wyrażenia regularne

- grep - pozwala wyszukiwać wzorce w tekście
- wykorzystywane jest to np:
  - do przeglądania logów
  - do przeszukiwania plików
  - do filtrowania wyników innych poleceń

## Grep i wyrażenia regularne

- `grep <wzorzec>` - wyszukuje wzorzec w wejściu standardowym
- `grep <wzorzec> <plik>` - wyszukuje wzorzec w pliku

## (bardzo) podstawowe wyrażenia regularne

- `.` - dowolny znak
- `*` - dowolna liczba poprzedzającego znaku
- `.*` - dowolna liczba dowolnych znaków
- `^` - początek linii
- `$` - koniec linii
- `[a-z],[abc],[0-9]` - dowolny znak z podanego zakresu

## Zadanie 5a - grep i wyrażenia regularne

::: nonincremental

- filtrowanie danych na standardowym wejściu
  ```
  grep "Marcin"
  ```
- wpisujemy losowe imiona, np:
  ```
  Kasia
  Zosia
  Marcin
  Maciek
  ```
- zakończ: `CTRL+c`

:::


## Zadanie 5b - przeszukiwanie listy użytkowników

::: nonincremental

- wyświetl wszystkich użytkowników z loginami 'user':
  ```
  grep "user" /etc/passwd
  ```
- wyświetl użytkowników z jednocyfrowymi parzystymi numerami:
  ```
  grep "^user[02468]:" /etc/passwd
  ```
- wyświetl loginy zaczynające się na 'user':
  ```
  grep "^user" /etc/passwd
  ```

:::

## Standardowe wejście - klawiatura, potok, plik

- standardowe wejście - ujednolicone źródło danych dla programów
- domyślnie jest to klawiatura
- można przekierować standardowe wejście na plik
- można przekierować standardowe wejście z jednego programu na standardowe wejście innego programu
- przekierowanie między programami nazywa się potokiem
- potok tworzy się za pomocą znaku `|`

## Zadanie 5c - przeglądanie logów serwera WWW

::: nonincremental

- wyświetl linie z logu, które zwracają kod 404:  
  ```
  cat /var/log/apache2/<userX>_access.log | grep " 404 "
  ```

- wyświetl nowe linie z logu, które zwracają pliki z rozszerzeniem .jpg:  
  ```
  tail -F /var/log/apache2/<login>_access.log | grep "\.jpg"
  ```

:::

## Uprawnienia do plików i katalogów

- każdy plik i katalog ma właściciela i grupę
- każdy plik i katalog ma zestaw uprawnień, które dzieją się na 3 grupy
- uprawnienia można zmieniać za pomocą polecenia `chmod`
- uprawnienia można sprawdzać np za pomocą polecenia `ls -l`


## Uprawnienia do plików i katalogów

- uprawnienia dzielą się na:
  - uprawnienia właściciela (u)
  - uprawnienia grupy (g)
  - uprawnienia innych (o)
- typy uprawnień:
  - odczyt (read)
  - zapis (write)
  - wykonanie (execute)


## Uprawnienia do plików i katalogów
- przykład:  
`-rw-r--r-- index.html`
- zmiana uprawnień:  
`chmod u+x index.html`
- `-rwxr--r-- index.html`

## Uprawnienia do plików i katalogów

- przykład:  
`-rw-r--r-- index.html`
- zmiana uprawnień:  
`chmod 640 index.html`
- `-rw-r----- index.html`
- 640 jest w systemie ósemkowym
- 640 = 110 100 000 = `rw- r-- ---`

## Zadanie 6 - poprawienie uprawnień do plików

::: nonincremental

- spróbuj przejść do strony `Ticket Details`
- sprawdź komunikat błędu w logach (`<userX>_error.log`)
- dodaj uprawnienia do odczytu dla odpowiedniego pliku
- serwer WWW działa w grupie `www-data`

:::
## Zadanie 6 - poprawienie uprawnień do plików

::: nonincremental

- zlokalizowanie pliku z niepoprawnymi uprawnieniami:  
  ```
  cat /var/log/apache2/<userX>_error.log
  ```
- sprawdź uprawnienia do pliku:  
  ```
  ls -l ticket-details.html
  ```
- popraw uprawnienia do pliku:  
  ```
  chmod g+r ticket-details.html
  ```

:::

## Przydatne polecenia przy instalacji aplikacji

- `wget <url>` - program do pobierania plików z internetu
- `tar` - program do archiwizacji plików
- `tar -xzf <archiwum>` - rozpakowuje archiwum tar.gz

## Zadanie 7 - instalacja bloga Wordpress

::: nonincremental

- przejdź do katalogu ze stroną WWW:  
  ```
  cd /var/www/html/<userX>
  ```
- pobierz bloga Wordpress:  
  ```
  wget https://wordpress.org/latest.tar.gz
  ```
- rozpakuj archiwum:
  ```
  tar -xzf latest.tar.gz
  ```
http://&lt;userX&gt;.warsztaty.linux.org.pl/wordpress/

:::

## Zadanie 7 - instalacja bloga Wordpress

::: nonincremental

- dane konfiguracyjne do bazy danych znajdują się w pliku `/tmp/baza.txt`

- po podaniu danych, otrzymamy komunikat, że Wordpress nie może zapisać pliku konfiguracyjnego.  

- dodać uprawnienia do zapisu dla katalogu Wordpress:  
  ```
  chmod g+w wordpress
  ```

- odświeżyć stronę i kontynuować instalację

:::

## Uruchamianie programów

- programy uruchamiany podając ich ścieżkę i nazwę
- ścieżka może być względna lub bezwzględna
- ścieżkę można pominąć, jeśli program znajduje się w katalogu, który jest w zmiennej środowiskowej PATH
- chcąc uruchomić program z bieżącego katalogu, można podać ścieżkę względną:
  ```
  ./program
  ```

## Zadanie 7 - uruchomienie programu

::: nonincremental

- skopiuj program do katalogu domowego
- program znajduje się w katalogu:  
  ```
  /var/www/html/user0/v2/files/guess.py
  ```
- uruchom program
- popraw uprawnienia do pliku, jeśli będzie taka potrzeba

:::

## Zadanie 7 - uruchomienie programu

::: nonincremental

- przejdź do katalogu domowego:  
  ```
  cd
  ```
- kopiowanie programu:  
  ```
  cp /var/www/html/user0/v2/files/guess.py ./
  ```
- uruchomienie programu:  
  ```
  ./guess.py
  ```

:::

## Co dalej?

- podręcznik manuala:
  ```
  man <polecenie>
  ```
  np:
  ```
  man ls
  ```
- społeczności:
  Polska Grupa Użytkowników Linuksa
  https://discord.linux.org.pl

- praktyka, praktyka, praktyka (maszyna wirtualna, vps, Raspberry Pi)

## Pytania?
