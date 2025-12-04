import random

numery_zagadnien = [1,2,3,4,5,6,7,8,9]
osoby = [
    "Anna K",
    "Emilia W",
    "Kamil K",
    "Kamil S",
    "Konrad M",
    "Krzysztof G",
    "Natalia D",
    "Piotr D",
    "Agata"
]

random.shuffle(numery_zagadnien)

print(numery_zagadnien)

for i in range(len(numery_zagadnien)):
    print(f'Osoba: {osoby[i]} wylosowała zagadnienie nr: {numery_zagadnien[i]}')

