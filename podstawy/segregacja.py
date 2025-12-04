import random as r

lista = []

for i in range(30):
    lista.append(r.randint(1,60))


print(lista)

parzyste = []
nieparzyste = []

print(15%5) #zwraca resztę z której nie udało się stworzyć pełnej wartości przy dzieleniu
print(4%2)

for i in range(len(lista)): # wykona się 30 razy bo rozmiar listy = 30
    sprawdziany_element = lista[i]
    if sprawdziany_element % 2 == 0:
        parzyste.append(sprawdziany_element)
    else:
        nieparzyste.append(sprawdziany_element)

print("parzyste: ", parzyste)
print("nieparzyste: ", nieparzyste)

    