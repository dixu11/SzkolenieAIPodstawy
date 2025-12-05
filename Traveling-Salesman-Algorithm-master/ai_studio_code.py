import pygame
import random
import math
import time

# --- KONFIGURACJA ---
WIDTH, HEIGHT = 900, 600
BG_COLOR = (30, 30, 30)
CITY_COLOR = (200, 200, 200)
PATH_COLOR = (0, 255, 128)
TEXT_COLOR = (255, 255, 255)
UI_BG_COLOR = (50, 50, 50)

# Parametry Algorytmu Genetycznego
POPULATION_SIZE = 150
MUTATION_RATE = 0.05
ELITISM_COUNT = 5  # Ilu najlepszych przechodzi bez zmian

pygame.init()
pygame.display.set_caption("Wizualizacja TSP - Algorytm Genetyczny")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("Arial", 16)
large_font = pygame.font.SysFont("Arial", 24, bold=True)

# --- KLASY I FUNKCJE ---

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

def calculate_fitness(cities, order):
    """Oblicza całkowity dystans dla danej kolejności miast."""
    dist = 0
    for i in range(len(order)):
        city_a = cities[order[i]]
        city_b = cities[order[(i + 1) % len(order)]] # Pętla powrotna do początku
        dist += city_a.distance_to(city_b)
    return dist

def create_initial_population(pop_size, num_cities):
    """Tworzy losową populację początkową."""
    population = []
    base_order = list(range(num_cities))
    for _ in range(pop_size):
        random.shuffle(base_order)
        population.append(base_order[:])
    return population

def crossover(parent1, parent2):
    """Krzyżowanie typu Order Crossover (OX) dla permutacji."""
    size = len(parent1)
    
    # Wybierz losowy wycinek od rodzica 1
    start = random.randint(0, size - 2)
    end = random.randint(start + 1, size - 1)
    
    child = [-1] * size
    child[start:end] = parent1[start:end]
    
    # Wypełnij resztę elementami z rodzica 2 w kolejności występowania
    current_p2_idx = 0
    for i in range(size):
        if child[i] == -1:
            while parent2[current_p2_idx] in child:
                current_p2_idx += 1
            child[i] = parent2[current_p2_idx]
            
    return child

def mutate(order):
    """Mutacja typu Swap - zamienia dwa losowe miasta."""
    if random.random() < MUTATION_RATE:
        idx1, idx2 = random.sample(range(len(order)), 2)
        order[idx1], order[idx2] = order[idx2], order[idx1]
    return order

def next_generation(cities, population):
    """Tworzy nowe pokolenie."""
    # 1. Ocena (Fitness) - sortujemy od najmniejszego dystansu
    ranked_pop = []
    for order in population:
        dist = calculate_fitness(cities, order)
        ranked_pop.append((dist, order))
    
    ranked_pop.sort(key=lambda x: x[0])
    
    # Najlepsze rozwiązania przechodzą dalej (elityzm)
    new_population = [x[1] for x in ranked_pop[:ELITISM_COUNT]]
    
    # Reszta populacji poprzez krzyżowanie
    # Używamy prostej selekcji: bierzemy z najlepszych 50% populacji
    mating_pool = [x[1] for x in ranked_pop[:len(population)//2]]
    
    while len(new_population) < len(population):
        parent1 = random.choice(mating_pool)
        parent2 = random.choice(mating_pool)
        child = crossover(parent1, parent2)
        child = mutate(child)
        new_population.append(child)
        
    best_dist = ranked_pop[0][0]
    best_order = ranked_pop[0][1]
    
    return new_population, best_order, best_dist

# --- GŁÓWNA PĘTLA ---

def main():
    clock = pygame.time.Clock()
    running = True
    
    # Stan aplikacji
    cities = []
    
    # Generuj domyślne 10 miast
    for _ in range(10):
        cities.append(City(random.randint(50, WIDTH-50), random.randint(50, HEIGHT-100)))

    population = []
    best_path = []
    best_distance = float('inf')
    generation = 0
    
    is_solving = False
    slow_mode = False
    start_time = 0
    elapsed_time = 0

    while running:
        screen.fill(BG_COLOR)
        
        # --- LOGIKA ---
        
        if is_solving:
            # Algorytm Genetyczny
            if not population:
                population = create_initial_population(POPULATION_SIZE, len(cities))
            
            population, best_path, best_distance = next_generation(cities, population)
            generation += 1
            elapsed_time = time.time() - start_time
            
            if slow_mode:
                time.sleep(0.1) # Spowolnienie
        else:
            # Jeśli nie rozwiązujemy, zresetuj licznik czasu, żeby nie biegł w tle
            if start_time == 0: elapsed_time = 0

        # --- RYSOWANIE ---
        
        # Rysowanie ścieżki
        if len(cities) > 1:
            points_to_draw = []
            order_to_use = best_path if best_path and len(best_path) == len(cities) else list(range(len(cities)))
            
            for idx in order_to_use:
                points_to_draw.append((cities[idx].x, cities[idx].y))
            
            # Zamknij pętlę
            if len(points_to_draw) > 0:
                points_to_draw.append(points_to_draw[0])
                pygame.draw.lines(screen, PATH_COLOR, False, points_to_draw, 2)

        # Rysowanie miast
        for city in cities:
            pygame.draw.circle(screen, CITY_COLOR, (city.x, city.y), 6)
            pygame.draw.circle(screen, (0,0,0), (city.x, city.y), 6, 1)

        # Rysowanie UI (Panel dolny)
        pygame.draw.rect(screen, UI_BG_COLOR, (0, HEIGHT-60, WIDTH, 60))
        
        status_text = "Działa" if is_solving else "Zatrzymany"
        mode_text = "Wolny" if slow_mode else "Szybki"
        
        infos = [
            f"Status: {status_text} (SPACJA)",
            f"Gen: {generation}",
            f"Dystans: {best_distance:.2f}",
            f"Czas: {elapsed_time:.2f}s",
            f"Tryb: {mode_text} (S)",
            f"Miasta: {len(cities)} (LPM: + / PPM: -)",
            f"Reset: (R)"
        ]
        
        for i, info in enumerate(infos):
            txt_surf = font.render(info, True, TEXT_COLOR)
            screen.blit(txt_surf, (20 + i * 120, HEIGHT - 40))

        if not is_solving and not best_path:
             inst = large_font.render("Naciśnij SPACJĘ aby rozpocząć", True, (255, 255, 0))
             screen.blit(inst, (WIDTH//2 - inst.get_width()//2, 50))

        # --- OBSŁUGA ZDARZEŃ ---
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_solving = not is_solving
                    if is_solving:
                        # Start/Wznowienie
                        if not population: # Jeśli to start od zera
                            start_time = time.time()
                            population = create_initial_population(POPULATION_SIZE, len(cities))
                        else: # Wznowienie - korygujemy start_time
                            start_time = time.time() - elapsed_time
                    
                if event.key == pygame.K_s:
                    slow_mode = not slow_mode
                    
                if event.key == pygame.K_r:
                    # Pełny reset
                    is_solving = False
                    cities = []
                    for _ in range(10):
                        cities.append(City(random.randint(50, WIDTH-50), random.randint(50, HEIGHT-100)))
                    population = []
                    best_path = []
                    best_distance = float('inf')
                    generation = 0
                    elapsed_time = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # Nie klikaj w panel UI
                if pos[1] < HEIGHT - 60:
                    if event.button == 1: # LPM - Dodaj miasto
                        cities.append(City(pos[0], pos[1]))
                        # Zmiana miast wymaga resetu populacji
                        is_solving = False
                        population = []
                        best_path = []
                        generation = 0
                        elapsed_time = 0
                        
                    elif event.button == 3: # PPM - Usuń najbliższe
                        if cities:
                            # Znajdź najbliższe miasto do kliknięcia
                            closest_city = min(cities, key=lambda c: math.hypot(c.x - pos[0], c.y - pos[1]))
                            if math.hypot(closest_city.x - pos[0], closest_city.y - pos[1]) < 30: # Tolerancja kliknięcia
                                cities.remove(closest_city)
                                is_solving = False
                                population = []
                                best_path = []
                                generation = 0
                                elapsed_time = 0

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()