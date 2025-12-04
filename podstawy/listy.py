lista1 = [1,2,45,34,777,10]
lista2 = list() #list(lista1) zapis przydatny np gdy chcemy zrobić jedną listę na start z wartościami drugiej
lista2.append(7)
lista2.append(8)
lista2.append(4)

print(lista1)
print(lista2)
print(lista1 + lista2)
print(lista1 *3)
print(lista1[-1]) #ostatnia wartość
print(lista1[1:3]) #wycinamy od pewngo indeksu do jeden mniej tutaj da: (1,2)
print(lista1[2:]) #puste -> do końca

print(len(lista1))



