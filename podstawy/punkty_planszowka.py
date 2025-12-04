
podano = 0
suma = 0
while podano != 'koniec':
    suma += int(podano)
    podano = input('Podaj kolejne punkty:')
    # if podano == 'koniec':
    #     break


print('Otrzymano punktów: ', suma)
print('Zakończono')