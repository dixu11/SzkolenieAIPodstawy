import random as r

print('hello')

#weight = int(input('Podaj wagę:'))
#heightM = float(input('Podaj wzrost:'))

weight = r.randint(80,120)
heightM = r.random(1.7,1.9)

print(f'input weight: {weight}')
print(f'input heightM: {heightM}')

bmi = weight / heightM**2
print(bmi)

overWeight = bmi>24.9
underWeight = bmi < 18.5
normalWeight = not overWeight and not underWeight
print(f'{overWeight}, {underWeight}, {normalWeight}')