

# slowo <warunek>:
#     instrukcja

numbers = [2,4,5,6]
print(numbers)
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])


#musimy wspierać się licznikiem
licznik = 0
while licznik < 4:
    print('Pozycja ', licznik)
    print(numbers[licznik])
    licznik+=1

#dokładnie to samo
for number in numbers:
    print(number)

# for number in :
#     print()

for i in range(20):
    print(i)

print('-----')

for i in range(5,21):
    print(i)


for i in range(5,21,3): # od 5 do 20 (1 mniej), co 3 liczby
    print(i)

for i in range(20,-1,-1): # od 20 do 0 co -1 
    print(i)