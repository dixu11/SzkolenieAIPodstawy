#1.6 Zdefiniuj listę 10 różnych liczb.
#  Napisz program, który odnajdzie najmniejszą i największą liczbę w zbiorze. Wykorzystaj pętlę for. 

liczby = [23,45,1,6,-7,-2,100,500,1000,5]

najwieksza = ''
najmniejsza = ''

for liczba in liczby:
    if najwieksza == '':
        najwieksza = liczba
    elif najwieksza < liczba:
        najwieksza = liczba
        
    if najmniejsza == '':
        najmniejsza = liczba
    elif najmniejsza > liczba:
        najmniejsza = liczba

    print(f'Największa: {najwieksza} i najmniejsza: {najmniejsza}')

    
