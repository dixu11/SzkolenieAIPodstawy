# while

import random

losowa = 0
licznik = 0
suma_oczek = 0

while losowa< 6:
    #licznik = licznik + 1
    licznik += 1
    losowa = random.randint(1,6)
    suma_oczek += losowa 
    print(f'Losowanie nr {licznik}, wypadło {losowa}')
    print('Nie trafiłeś 6 próbuj dalej')

print('wolosowałeś 6! Koniec programu')
print('Wymagało ',licznik,'losowań')
print(f'Było {licznik} losowań, łącznie wypadło {suma_oczek}')


# if losowa<6:
#     print(losowa)
#     print('Nie trafiłeś 6 próbuj dalej')