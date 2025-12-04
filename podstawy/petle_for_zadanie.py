# wylosować 100 liczb i obliczyć średnią

import random

sum = 0
zakres = 100_000

for i in range(zakres):
    value = random.randint(0,100)
    #print(value)
    sum += value

print(f'Średnia wynosi {sum/zakres:.5}')