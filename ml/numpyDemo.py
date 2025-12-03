import numpy as np

lista = [1,2,3]
tablica = np.array([1,2,3])

print(lista)
print(tablica)
print(type(lista))
print(type(tablica))

print(tablica.shape)

wielowymiarowa = np.array([[11,22,33], [1,2,3]])
print(wielowymiarowa.shape)

print(tablica * 2)
print(tablica * 10)
print(tablica ** 2)

lista2 = [1,2,3]
lista2 = [el + 10 for el in lista2]
print(lista2)

tablica2 = np.array([160,170,180,190,200])
print(tablica2.min())
print(tablica2.max())
print(tablica2.std())

print(tablica2[0])  
print(tablica2[1:4]) 
print(tablica2[-1])

X = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(X[0, 0])   # 1
print(X[1, :])   # [4 5 6]  -> cały drugi wiersz
print(X[:, 2])   # [3 6 9]  -> cała trzecia kolumna

hr = np.array([65, 72, 80, 78, 90, 85])

print(hr.mean())
print(hr.max())
print(hr.min())
hr2 = hr +5
print(hr2)
print(hr[hr>hr.mean()])
print(hr > hr.mean())