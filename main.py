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
***DONE*** 3. zakup - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt zostaje dodany do magazynu, jeśli go nie było. Obliczenia są wykonane odwrotnie do komendy "sprzedaz". 
Saldo konta po zakończeniu operacji „zakup” nie może być ujemne.
***DONE*** 4. konto - Program wyświetla stan konta.
***DONE*** 5. lista - Program wyświetla całkowity stan magazynu wraz z cenami produktów i ich ilością.
***DONE*** 6. magazyn - Program wyświetla stan magazynu dla konkretnego produktu. Należy podać jego nazwę.
***DONE*** 7. przegląd - Program pobiera dwie zmienne „od” i „do”, na ich podstawie wyświetla wszystkie wprowadzone akcje zapisane pod indeksami od „od” do „do”. 
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
inventory = {}


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


def check_if_number_positive(confirmation_status, number, message):
    if confirmation_status == False:
        return None
    else:
        if number <= 0:
            print(message)
            return None
        else:
            return number


def item_not_in_inventory():
    print("Nie ma takiego przedmiotu w magazynie.")
    print("Czy spróbować ponownie?")
    print("Tak: Y")
    print("Nie: N")
    user_confirm = str(input(": ")).upper()
    if user_confirm == "N":
        return False
    elif user_confirm == "Y":
        return True
    else:
        bad_response()


def buy():
    item_name = None
    while not isinstance(item_name, str):
        item_name = str(input("Podaj nazwe przedmiotu: "))
        item_name_confirm = confirm(item_name)
        if item_name_confirm == False:
            item_name = None
    balance_check = False
    while not balance_check:
        item_quantity = None
        while not isinstance(item_quantity, int):
            try:
                item_quantity = int(
                    input("Podaj liczbe zakupionych przedmiotów: "))
                item_quantity_confirm = confirm(item_quantity)
                item_quantity = check_if_number_positive(
                    item_quantity_confirm, item_quantity, "Bład. Liczba kupowanych sztuk nie może być mniejsza lub równa 0.")
            except ValueError:
                bad_response()
        cost_price = None
        while not isinstance(cost_price, float):
            try:
                cost_message = "Podaj cenę zakupu dla jednej sztuki towaru: "
                cost_price = decimal_count_check(cost_price, cost_message)
                cost_confirm = confirm(cost_price)
                cost_price = check_if_number_positive(
                    cost_confirm, cost_price, "Bład. Cena zakupu nie może być mniejsza lub równa 0.")
            except ValueError:
                bad_response()
        purchase_price = item_quantity * cost_price
        if account_balance - purchase_price < 0:
            print(
                f"Błąd. Nie można zakupić przedmiotu \"{item_name}\" w ilości: {item_quantity}, ponieważ saldo konta nie może być ujemne")
            print("Spróbuj ponownie.")
            cost_price = None
            item_quantity = None
            balance_check = False
        else:
            balance_check = True
    list_price = None
    while not isinstance(list_price, float):
        try:
            list_message = "Podaj docelową cene sprzedaży 1 sztuki towaru: "
            list_price = decimal_count_check(list_price, list_message)
            list_price_confirm = confirm(list_price)
            list_price = check_if_number_positive(
                list_price_confirm, list_price, "Bład. Cena sprzedaży nie może być mniejsza lub równa 0.")
        except ValueError:
            bad_response()
    history_message = f"Zakupiono przedmiot: \"{item_name}\", w ilości: {item_quantity}. Cena za sztuke: {round(cost_price, 2)} PLN. Łączna cena za zamówienie: {round(purchase_price, 2)} PLN. Cene sprzedaży produktu ustalono na: {round(list_price, 2)} PLN."
    history.append(history_message)
    print(history_message)
    if item_name.upper() not in inventory:
        inventory[item_name.upper()] = {
            "item_name": item_name,
            "list_price": list_price,
            "quantity": item_quantity
        }
    else:
        inventory[item_name.upper()]["list_price"] = list_price
        inventory[item_name.upper()]["quantity"] += item_quantity
    available_item_quantity = inventory.get(
        item_name.upper(), {}).get("quantity")
    print(
        f"Dostępna ilość przedmiotu \"{item_name}\": {available_item_quantity}")
    return purchase_price


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


def list_overview():
    print("*" * 30)
    print("PEŁEN WYKAZ MAGAZYNU")
    print("*" * 10)
    for item_name in inventory:
        name = inventory.get(item_name, {}).get("item_name")
        quantity = inventory.get(item_name, {}).get("quantity")
        list_price = inventory.get(item_name, {}).get("list_price")
        print("*" * 10)
        print(f"Przedmiot: {name}")
        print(f"Liczba dostępnych sztuk: {quantity}")
        print(f"Cena: {round(list_price, 2)} PLN")
    print("*" * 30)


def inventory_overview():
    item = None
    while not item:
        item = str(input("Podaj nazwe przedmiotu: ")).upper()
        if item not in inventory:
            user_confirm = item_not_in_inventory()
            if not user_confirm:
                break
            else:
                item = None
        else:
            quantity = inventory[item]["quantity"]
            name = inventory.get(item, {}).get("item_name")
            print(f"Stan magazynu dla przedmiotu \"{name}\": {quantity}.")


def sell():
    item_to_sell = None
    while not item_to_sell:
        item_to_sell = str(
            input("Podaj nazwe przedmiotu, który chcesz sprzedać: ")).upper()
        if item_to_sell not in inventory:
            user_confirm = item_not_in_inventory()
            if not user_confirm:
                break
            else:
                item_to_sell = None
        else:
            item_name = inventory.get(item_to_sell, {}).get("item_name")
            list_price = inventory.get(item_to_sell, {}).get("list_price")
            quantity = inventory.get(item_to_sell, {}).get("quantity")
            print(
                f"Przedmiot \"{item_name}\". Liczba dostępnych sztutk: {quantity}. Cena sprzedaży: {round(list_price, 2)} PLN.")
            quantity_to_sell = None
            while not quantity_to_sell:
                try:
                    quantity_to_sell = int(
                        input("Podaj liczbe sprzedawanych sztuk: "))
                    quantity_to_sell_confirm = confirm(quantity_to_sell)
                    quantity_to_sell = check_if_number_positive(
                        quantity_to_sell_confirm, quantity_to_sell, "Bład. Liczba sprzedawanych sztuk nie może być mniejsza lub równa 0.")
                    if isinstance(quantity_to_sell, int):
                        if quantity - quantity_to_sell < 0:
                            print(
                                "Bład. Liczba sprzedawanych sztuk, przekracza liczbę sztuk dostępnych na magazynie.")
                            quantity_to_sell = None
                except ValueError:
                    bad_response()
        if not user_confirm:
            break
        message = f"Przedmiot: {item_name}. Liczba sprzedawanych sztuk: {quantity}. Cena sprzedaży za sztukę: {round(list_price, 2)} PLN. Pozostanie: {quantity - quantity_to_sell}"
        user_confirm = confirm(message)
        if not user_confirm:
            break
        else:
            selling_price = quantity_to_sell * list_price
            quantity_left = quantity - quantity_to_sell
            inventory[item_to_sell]["quantity"] = quantity_left
            history_message = f"Sprzedano przedmiot \"{item_name}\" w liczbie: {quantity_to_sell}. Łączna cena sprzedaży: {round(selling_price, 2)}."
            history.append(history_message)
            return selling_price


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
                account_balance += sell()
                account_balance_note()
                command_check = False
            elif command == 3:
                account_balance -= buy()
                account_balance_note()
                command_check = False
            elif command == 4:
                account_balance_note()
                command_check = False
            elif command == 5:
                list_overview()
                command_check = False
            elif command == 6:
                inventory_overview()
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
