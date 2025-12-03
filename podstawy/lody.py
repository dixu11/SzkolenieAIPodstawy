# Przygotuj program, w którym wypiszesz rachunek za lody.
# Program drukuje ile gałek lodów kupił klient, jaka jest cena za gałkę lodów. 
# Za każde 2 gałki program nalicza zniżkę 1zł. 
# Wypisz cenę po zniżce. 
# Zmiana ceny za gałkę powinna wymagać jednej modyfikacji w kodzie (wykorzystaj zmienne)

ilosc_lodow = 2
cena_galki = 5
promocja = -1

print('Wybrałeś ', ilosc_lodow ,' lodów')
print('Cena za gałkę: ' , cena_galki, "zł")
cena_lodow = ilosc_lodow * cena_galki
print('Koszt: ' , cena_lodow , "zł")
promocja_zl = ilosc_lodow // 2 * promocja
print( 'Cena z promocją ',  promocja_zl + cena_lodow , 'zł' )

duzy = ilosc_lodow >= 3
maly = ilosc_lodow == 1

print(f'Duży lód: {duzy}')
print(f'Czy mały? {maly}')
print(f'Sredni: {not maly and not duzy}')
print(f'Mały lub duży? {maly or duzy}')

#not and or

print('Wybrałeś ', ilosc_lodow ,' lodów')
print(f'Wybrałeś {ilosc_lodow} lodów')


print('Cena za gałkę: ' , cena_galki, "zł")
cena_lodow = ilosc_lodow * cena_galki
print('Koszt: ' , cena_lodow , "zł")
promocja_zl = ilosc_lodow // 2 * promocja

print( 'Cena z promocją ',  promocja_zl + cena_lodow , 'zł' )
print(f'Cena z promocją {promocja_zl+cena_lodow} zł')