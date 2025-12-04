def przywitaj_osobe(imie_osoby, wiek=18, tytul=""):
    if wiek > 60:
        print(f'Dzień dobry {tytul} {imie_osoby}')
    else:
        print(f'Cześć {tytul} {imie_osoby}')

print('Zaczynamy program')
przywitaj_osobe('Wojtek',15)
przywitaj_osobe('Ania',30)
przywitaj_osobe('Zofia',80)
przywitaj_osobe('Zofia',80)
przywitaj_osobe('Marta')
przywitaj_osobe('Marian',tytul='profesor')

import random

print(random.randint(1,6))
wynik_losowania= random.randint(1,6)

def sumuj_liczby(number1, number2):
    #print(number1 + number2)
    return number1 + number2

wynik = sumuj_liczby(10,15)

print(f'wynik to: {wynik * 1.07:.6} (w tym 7% watu)')







