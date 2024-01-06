import math


def Proste():
    x = int(input("Podaj pierwszą liczbę: "))
    y = int(input("Podaj drugą liczbę: "))

    def dodawanie():
        suma_dodawania= x + y
        print(suma_dodawania)

    def odejmowanie():
        suma_odejmowania = x - y
        print(suma_odejmowania)

    def mnożenie():
        suma_mnożenia = x * y
        print(suma_mnożenia)

    def dzielenie():
        suma_dzielenia = x / y
        print(int(suma_dzielenia))

    pytanie = int(input("Wpisz 1, aby dodawać. 2, aby odejmować. 3, aby mnożyć. 4, aby dzielić"))

    if pytanie == 1:
        dodawanie()
    elif pytanie == 2:
        odejmowanie()
    elif pytanie == 3:
        mnożenie()
    elif pytanie == 4:
        dzielenie()
    else:
        print("Nieprawidłowe dane!")

def Potegi():
    x = int(input("Wpisz liczbę, którą chcesz podnieść do potęgi: "))

    def oblicz_potege():
            obliczona_potega = x*x
            print(obliczona_potega)
    print(oblicz_potege())

def Pierwiastki():
    Liczba_pierwiastkowana = int(input("Podaj liczbę, którą chcesz pierwiastkować"))

    def Oblicz_pierwiastek():
        Obliczony_pierwiastek = math.sqrt(Liczba_pierwiastkowana)
        print(Obliczony_pierwiastek)
    print(Oblicz_pierwiastek())



Witaj = int(input("Witaj w kalkulatorze!, wpisz 1, aby wykonać proste działania, wpisz 2 aby potęgować, wpisz 3 aby pierwiastkować "))

if Witaj == 1:
    Proste()
elif Witaj == 2:
    Potegi()
elif Witaj == 3:
    Pierwiastki()
else:
    print("Zły input!")


    
