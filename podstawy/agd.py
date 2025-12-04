# 1.3 W sklepie ze sprzętem AGD oferowana jest sprzedaż ratalna. 
# Napisz program umożliwiający wyliczenie wysokości miesięcznej raty za zakupiony sprzęt.  Danymi wejściowymi dla programu są: 
# • cena towaru (od 100 zł do 10 tys. zł), 
# • liczba rat (od 6 do 48). 
# Program powinien sprawdzać, czy podane dane mieszczą się w określonych powyżej zakresach, a w przypadku błędu wyświetlać stosowny komunikat i natychmiast zakończyć działanie programu. (użyj instrukcji return)
# Kredyt jest oprocentowany w zależności od liczby rat:
#  • od 6–12 wynosi 2.5% , 
# • od 13–24 wynosi 5%, 
# • od 25–48 wynosi 10%. 
# Obliczona miesięczna rata powinna zawierać również odsetki. 


cena_towaru_zl = int(input('Podaj cenę od 100 - 10 000zł'))

if cena_towaru_zl < 100 or cena_towaru_zl > 10_000:
    print('Cena ze złego przedziału')
    exit()

ilosc_rat = int(input('Podaj ilość rat od 6-48'))

if ilosc_rat <6 or ilosc_rat > 48:
    print('bledna ilość rat')
    exit()

jedna_rata_cena = cena_towaru_zl / ilosc_rat

oprocentowanie = 0
if ilosc_rat <= 12:
    oprocentowanie = 0.025
elif ilosc_rat <= 24:
    oprocentowanie = 0.05
else:
    oprocentowanie = 0.1

print(f'Oprocentowanie{oprocentowanie * 100}%')
print(f'Jedna rata z oprocentowaniem wynosi: {(oprocentowanie + 1) * jedna_rata_cena} zł')


# if 6 <= ilosc_rat <= 12:
#     oprocentowanie = 0.025
# elif 14 <= ilosc_rat <= 24:
#     oprocentowanie = 0.05
# elif 25 <= ilosc_rat <= 48:
#     oprocentowanie = 0.1


# if cena_towaru_zl < 10_000 and cena_towaru_zl > 100:
#     print('cena jest ok')

# if  10_000 < cena_towaru_zl < 100 :
#     print('cena jest ok')