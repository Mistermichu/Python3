'''
Napisz program, który będzie rejestrował operacje na koncie firmy i stan magazynu.

Program po uruchomieniu wyświetla informację o dostępnych komendach:
-Saldo
-Sprzedaż
-Zakup
-Konto
-Lista
-Magazyn
-Przegląd
-Koniec


Po wprowadzeniu odpowiedniej komendy, aplikacja zachowuje się w unikalny sposób dla każdej z nich:
***DONE*** 1. saldo - Program pobiera kwotę do dodania lub odjęcia z konta.
2. sprzedaż - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt musi znajdować się w magazynie. 
Obliczenia respektuje względem konta i magazynu (np. produkt "rower" o cenie 100 i jednej sztuce spowoduje odjęcie z magazynu produktu "rower" oraz dodanie do konta kwoty 100).
3. zakup - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt zostaje dodany do magazynu, jeśli go nie było. Obliczenia są wykonane odwrotnie do komendy "sprzedaz". 
Saldo konta po zakończeniu operacji „zakup” nie może być ujemne.
***DONE*** 4. konto - Program wyświetla stan konta.
5. lista - Program wyświetla całkowity stan magazynu wraz z cenami produktów i ich ilością.
6. magazyn - Program wyświetla stan magazynu dla konkretnego produktu. Należy podać jego nazwę.
7. przegląd - Program pobiera dwie zmienne „od” i „do”, na ich podstawie wyświetla wszystkie wprowadzone akcje zapisane pod indeksami od „od” do „do”. 
Jeżeli użytkownik podał pustą wartość „od” lub „do”, program powinien wypisać przegląd od początku lub/i do końca. 
Jeżeli użytkownik podał zmienne spoza zakresu, program powinien o tym poinformować i wyświetlić liczbę zapisanych komend (żeby pozwolić użytkownikowi wybrać odpowiedni zakres).
***DONE*** 8. koniec - Aplikacja kończy działanie.

Dodatkowe wymagania:
- Aplikacja od uruchomienia działa tak długo, aż podamy komendę "koniec".
- Komendy saldo, sprzedaż i zakup są zapamiętywane przez program, aby móc użyć komendy "przeglad".
- Po wykonaniu dowolnej komendy (np. "saldo") aplikacja ponownie wyświetla informację o dostępnych komendach, a także prosi o wprowadzenie jednej z nich.
- Zadbaj o błędy, które mogą się pojawić w trakcie wykonywania operacji (np. przy komendzie "zakup" jeśli dla produktu podamy ujemną kwotę, 
aplikacja powinna wyświetlić informację o niemożności wykonania operacji i jej nie wykonać).
- Zadbaj też o prawidłowe typy danych.
'''
account_balance = 0
history = []
warehouse = {}


def menu():
    print("*" * 100)
    print("WYBIERZ AKCJE:")
    print("Saldo: 1")
    print("Sprzedaż: 2")
    print("Zakup: 3")
    print("Konto: 4")
    print("Lista: 5")
    print("Magazyn: 6")
    print("Przeglad: 7")
    print("Koniec: 8")
    print("*" * 100)


def account_balance_note():
    print(f"Obecny stan konta: {round(account_balance,2)} PLN")


def bad_response():
    print("*" * 10)
    print("Blad.")
    print("Sprobuj ponownie.")
    print("*" * 10)


def confirm(user_input):
    user_confirm = True
    while user_confirm:
        print(f"Czy podana wartosc: \"{user_input}\" jest poprawna?")
        print("Tak: Y")
        print("Nie: N")
        confirm_input = (input(": ")).upper()
        if confirm_input == "Y":
            user_confirm = False
            return True
        elif confirm_input == "N":
            user_confirm = True
            return False
        else:
            bad_response()
            user_confirm = True


def history_overview():
    if len(history) == 0:
        print("Nie wykonano żadnych operacji.")
    else:
        start = None
        while not isinstance(start, int):
            try:
                print("Podaj początkowy krok przeglądu.")
                print("Wprowadz 0 aby wyswietlić od początku.")
                start = int(input(": "))
                if start < 0:
                    bad_response()
                    start = None
                elif start > len(history):
                    print(
                        f"Bład. Dotychczasowa liczba wykonanych kroków: {len(history)}")
                    start = None
            except ValueError:
                bad_response()
                start = None
        stop = None
        while not isinstance(stop, int):
            try:
                print("Podaj końcowy krok przeglądu.")
                print("Wprowadz 0 aby wyswietlić do końca.")
                stop = int(input(": "))
                if stop < 0:
                    bad_response()
                    stop = None
                elif stop == 0:
                    stop = len(history)
                elif stop < start:
                    print(
                        "Błąd. Krok końcowy nie może być mniejszy niż krok początkowy.")
                    stop = None
                elif stop > len(history):
                    print(
                        f"Bład. Dotychczasowa liczba wykonanych kroków: {len(history)}")
                    stop = None
            except ValueError:
                bad_response()
        if start >= 1:
            start -= 1
        if stop == 0:
            stop = None
        print("*" * 10 + " HISTORIA " + "*" * 10)
        for step, message in enumerate(history[start:stop]):
            print(f"{step + start + 1}.: {message}")
        print("*" * 30)


'''3. zakup - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt zostaje dodany do magazynu, jeśli go nie było. Obliczenia są wykonane odwrotnie do komendy "sprzedaz". 
Saldo konta po zakończeniu operacji „zakup” nie może być ujemne.'''


def decimal_count_check(number, message):
    decimal_count = 3
    while decimal_count > 2:
        number = float(
            input(message).replace(",", "."))
        decimal_count = len(str(number).split(".")[1])
        if decimal_count > 2:
            bad_response()
        else:
            return number


def buy():
    item_name = str(input("Podaj nazwe przedmiotu: "))
    cost_price = None


def balance():
    amount = None
    while not isinstance(amount, float):
        try:
            balance_message = "Podaj kwote do dodania/odjecia z konta: "
            amount = decimal_count_check(amount, balance_message)
            amount_confirm = confirm(amount)
            if amount_confirm == True:
                if amount > 0:
                    history_message = f"Do konta dodano: {amount} PLN."
                    history.append(history_message)
                elif amount < 0:
                    history_message = f"Z konta odjęto: {amount} PLN."
                    history.append(history_message)
                return amount
            if amount_confirm == False:
                amount = None
        except ValueError:
            bad_response()


run = True
while run:
    command_check = True
    while command_check:
        menu()
        try:
            command = int(input(": "))
            if command == 1:
                account_balance += balance()
                account_balance_note()
                command_check = False
            elif command == 2:
                print("Komenda 2")
                command_check = False
            elif command == 3:
                print("Komenda 3")
                command_check = False
            elif command == 4:
                print("Obecny stan konta:")
                print(f"{round(account_balance,2)} PLN")
                command_check = False
            elif command == 5:
                print("Komenda 5")
                command_check = False
            elif command == 6:
                print("Komenda 6")
                command_check = False
            elif command == 7:
                history_overview()
                command_check = False
            elif command == 8:
                command_check = False
                run = False
            else:
                bad_response()
        except ValueError:
            bad_response()
