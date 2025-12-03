waga = 80
wzrost = 1.8
bmi = waga / wzrost **2
print(f'waga: {waga} wzrost {wzrost} bmi {bmi}')
#24,9 - nadwaga  lub czy BMI jest poniżej 18,5 - niedowaga.
nadwaga = bmi > 24.9
niedowaga = bmi < 18.5
normalna_waga = not nadwaga and not niedowaga
print(f'Nadwaga:{nadwaga} Niedowaga:{niedowaga} Normalna waga:{normalna_waga}')