




ilosc_lodow = 2
cena_galki = 4.5
godzina = 10
promocja = -1
promocja = godzina < 15

#typy w pythonie
print(type(ilosc_lodow))
print(type(234))
print(type(cena_galki))
print(promocja)
print(type(promocja))
print(type('123'))
print(type([2,4,56]))






print('Wybrałeś ', ilosc_lodow ,' lodów')
print('Cena za gałkę: ' , cena_galki, "zł")
cena_lodow = ilosc_lodow * cena_galki
print('Koszt: ' , cena_lodow , "zł")
promocja_zl = ilosc_lodow // 2 * promocja
print( 'Cena z promocją ',  promocja_zl + cena_lodow , 'zł' )