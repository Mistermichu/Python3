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
1. saldo - Program pobiera kwotę do dodania lub odjęcia z konta.
2. sprzedaż - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt musi znajdować się w magazynie. 
Obliczenia respektuje względem konta i magazynu (np. produkt "rower" o cenie 100 i jednej sztuce spowoduje odjęcie z magazynu produktu "rower" oraz dodanie do konta kwoty 100).
3. zakup - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt zostaje dodany do magazynu, jeśli go nie było. Obliczenia są wykonane odwrotnie do komendy "sprzedaz". 
Saldo konta po zakończeniu operacji „zakup” nie może być ujemne.
4. konto - Program wyświetla stan konta.
5. lista - Program wyświetla całkowity stan magazynu wraz z cenami produktów i ich ilością.
6. magazyn - Program wyświetla stan magazynu dla konkretnego produktu. Należy podać jego nazwę.
7. przegląd - Program pobiera dwie zmienne „od” i „do”, na ich podstawie wyświetla wszystkie wprowadzone akcje zapisane pod indeksami od „od” do „do”. 
Jeżeli użytkownik podał pustą wartość „od” lub „do”, program powinien wypisać przegląd od początku lub/i do końca. 
Jeżeli użytkownik podał zmienne spoza zakresu, program powinien o tym poinformować i wyświetlić liczbę zapisanych komend (żeby pozwolić użytkownikowi wybrać odpowiedni zakres).
8. koniec - Aplikacja kończy działanie.

Dodatkowe wymagania:
- Aplikacja od uruchomienia działa tak długo, aż podamy komendę "koniec".
- Komendy saldo, sprzedaż i zakup są zapamiętywane przez program, aby móc użyć komendy "przeglad".
- Po wykonaniu dowolnej komendy (np. "saldo") aplikacja ponownie wyświetla informację o dostępnych komendach, a także prosi o wprowadzenie jednej z nich.
- Zadbaj o błędy, które mogą się pojawić w trakcie wykonywania operacji (np. przy komendzie "zakup" jeśli dla produktu podamy ujemną kwotę, 
aplikacja powinna wyświetlić informację o niemożności wykonania operacji i jej nie wykonać).
- Zadbaj też o prawidłowe typy danych.
'''
user_action = []
account_balance = 0
warehouse = {}


def menu():
    print("*" * 100)
    print("Wybierz akcje:")
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
    print(f"Obecny stan konta: {account_balance} PLN")


def bad_response():
    print("Blad.")
    print("Sprobuj ponownie.")


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


def balance():
    amount = None
    while not isinstance(amount, float):
        try:
            amount = float(input("Podaj kwote do dodania/odjecia z konta: "))
            amount_confirm = confirm(amount)
            if amount_confirm == True:
                return amount
            if amount_confirm == False:
                amount = None
        except ValueError:
            bad_response()


run = True
while run:
    menu()
    command_check = True
    while command_check:
        try:
            command = int(input(": "))
            if command == 1:
                account_balance_origin = account_balance
                account_balance += balance()
                if account_balance < 0:
                    print("Bład. Stan konta nie moze wynosic mniej niz 0.")
                    print("Operacja zostala odrzucona.")
                    account_balance = account_balance_origin
                    account_balance_note()
                    command_check = False
                else:
                    account_balance_note()
                    command_check = False
            elif command == 2:
                print("Komenda 2")
                command_check = False
            elif command == 3:
                print("Komenda 3")
                command_check = False
            elif command == 4:
                print("Komenda 4")
                command_check = False
            elif command == 5:
                print("Komenda 5")
                command_check = False
            elif command == 6:
                print("Komenda 6")
                command_check = False
            elif command == 7:
                print("Komenda 7")
                command_check = False
            elif command == 8:
                command_check = False
                run = False
            else:
                bad_response()
        except ValueError:
            bad_response()
