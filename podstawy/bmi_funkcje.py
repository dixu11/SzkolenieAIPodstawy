# 1.7 Przygotuj funkcję, która dla danego BMI będzie zwracać o ile skróci się przewidywana długość życia, jeśli mamy nadwagę. 
# Dla wagi normalnej i niedowagi zwraca 0. Dla BMI powyżej 30 zwraca 0,3 roku,
# między 27,5 a 30 zwraca 0,2 roku a między 27,5 a 24.9 zwraca 0,1 roku. 
# Możesz również napisać równanie matematyczne, które wygładzi zwracane wartości. 

# 1.8 Przygotuj nową funkcję, która przyjmie wagę, wzrost oraz ile planujemy schudnąć a 
# następnie zwróci o ile lat przedłuży to naszą przewidywaną długość życia. 
# Wykorzystaj w niej wcześniejszą funkcję. 


def calculate_final_lifetime_loss(weight, height):
    print(f'waga: {weight} wzrost {height}')
    final_years_lost = 0
    years_lost_per_kg = 1
    while years_lost_per_kg != 0:
        bmi = calculate_bmi(weight,height)
        years_lost_per_kg = shorter_life_by_per_kg(bmi)
        final_years_lost+= years_lost_per_kg
        print(f'Określono strate {years_lost_per_kg} przy {bmi} i wadze {weight}, łącznie {final_years_lost}') 
        weight-=1
    print('Łączna strata statystycznej dłogości życia przy takim bmi to: ', final_years_lost)


def calculate_bmi(weight,height):
    bmi = weight / height **2
    return bmi


def shorter_life_by_per_kg(bmi):
    if bmi > 30:
        return 0.3
    elif bmi > 27.5:
        return 0.2
    elif bmi > 24.9:
        return 0.1
    else:
        return 0
    

calculate_final_lifetime_loss(110,1.85)
    