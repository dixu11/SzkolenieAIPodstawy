cena = 3000
promocja = 0.05
ilosc_rat = 24
oprocentowanie = 0.01

print('Obniżka ceny pralki o 5%! Wcześniej kosztowała', cena , 'zł, teraz: ', cena * (1 - promocja), 'zł')
print('Pralka kosztuje ', cena , ' zł')
print('Raty 24x')
print('Koszt jednej raty:' , cena/ilosc_rat,"zł")
print('Oprocentowanie wynosi: 1%')
print('Rata z oprocentowaniem:', cena/ilosc_rat * (1 + oprocentowanie), "zł")