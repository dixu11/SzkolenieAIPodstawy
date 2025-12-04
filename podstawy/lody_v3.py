print('Ilość lodów: ')

ilosc_lodow = int(input()) # input zostawia zawsze tekst aby na tym liczyć trzeba przekonwertowac na float lub na int
print(type(ilosc_lodow))
cena_galki = 4.5
godzina = int(input('Podaj która godzina (tylko pełna godzina np. 15)'))

if godzina < 12:
    print('Wielka promocja')
    cena_galki = 3
elif godzina < 15:
    print('Weszla promocja za wczesną godzinę')
    cena_galki = 3.5
else:
    print("Ustawiono standardową cenę")

print('Wybrałeś ', ilosc_lodow ,' lodów')
print('Cena za gałkę: ' , cena_galki, "zł")
cena_lodow = ilosc_lodow * cena_galki
print('Koszt: ' , cena_lodow , "zł")
# promocja_zl = ilosc_lodow // 2 * promocja
# print( 'Cena z promocją ',  promocja_zl + cena_lodow , 'zł' )