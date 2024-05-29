@echo off

echo Witaj w programie!

REM Menu główne
:menu
echo Wybierz opcje:
echo 1 - Uruchom projekt
echo 2 - Informacje i instrukcja obslugi
echo 3 - Zakoncz

set /p option=""

if "%option%"=="1" (
    call :run_project
) else if "%option%"=="2" (
    call :show_info
) else if "%option%"=="3" (
    echo Zakonczono program.
    exit /b
) else (
    echo Nieprawidlowy wybor. Sprobuj ponownie.
    goto menu
)

pause
exit /b

REM Uruchomienie projektu
:run_project
python projekt.py
setlocal enabledelayedexpansion

REM Menu uruchamiania projektu
:run_project_menu
echo Gdzie chcesz wyswietlic wynik szyfrowania?
echo 1 - W konsoli
echo 2 - W pliku HTML
echo 3 - Powrot do menu glownego

set /p choice=""

REM Wyświetlenie danych
if "%choice%"=="1" (
    echo Wypisywanie danych z pliku output.txt:
    type output.txt
    goto :backing_up
) else if "%choice%"=="2" (
    echo Uruchamianie pliku HTML.
    start "" "http://127.0.0.1:5500/index.html"
    goto :backing_up
) else if "%choice%"=="3" (
    goto menu
) else (
    echo Wybor nieprawidlowy.
    goto run_project_menu
)

endlocal
goto :eof

REM Menu działania 2
:backing_up
echo 1 - Powrot do menu glownego
echo 2 - Zakoncz program

set /p choice=""
if "%choice%"=="1" (
    goto menu
) else if "%choice%"=="2" (
    echo Zakonczono program.
    exit /b
) else (
    echo Nieprawidlowy wybor.
    goto backing_up
)

REM Informacje i instrukcja obslugi
:show_info
echo Instrukcja obslugi:
echo Podaj tekst, ktory chcesz zaszyfrowac zgodnie z szyfrem Mendelejewa - zamiast kolejnych liter,
echo wypisywane sa liczby atomowe pierwiastka,
echo odstep miedzy literami zastepuje symbol gwiazdki *, a odstep miedzy wyrazami dwie gwiazdki **.
echo Zaszyfrowane nie moga zostac znaki specjalne typu !,*,# ani liczby, poniewaz mogloby to wprowadzic
echo bledy zwiazane z odczytem zaszyfrowanego tekstu.
echo 1 - Powrot do menu glownego

set /p choice=""
if "%choice%"=="1" (
    goto menu
) else (
    echo Nieprawidlowy wybor.
    goto show_info
)

goto :eof
