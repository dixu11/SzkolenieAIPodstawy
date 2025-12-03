cena = 4000
promocja = 0.05
ilosc_rat = 24
oprocentowanie = 0.01

print('Obniżka ceny pralki o 5%! Wcześniej kosztowała', cena , 'zł, teraz: ', cena * (1 - promocja), 'zł')
print('Pralka kosztuje ', cena , ' zł')
print('Raty 24x')
cena_raty = cena/ilosc_rat
print('Koszt jednej raty:' , cena_raty,"zł")
print('Oprocentowanie wynosi: 1%')
ostateczna_cena = cena_raty * (1 + oprocentowanie)
print(f'Rata z oprocentowaniem:{  ostateczna_cena:.6}zł') #z ilu wartości ma składać się liczbowy wynik
print(f'Rata z oprocentowaniem:{ format(ostateczna_cena,'.2f')}zł') # pełna kontrola nad liczbami po przecinku