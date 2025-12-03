print('hello')

weight = 110
heightM = 1.85

bmi = weight / heightM**2
print(bmi)

overWeight = bmi>24.9
underWeight = bmi < 18.5
normalWeight = not overWeight and not underWeight
print(f'{overWeight}, {underWeight}, {normalWeight}')
