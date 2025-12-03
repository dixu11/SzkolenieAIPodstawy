import time
import numpy as np
# -----------------------------------------
# Czysty Python
# -----------------------------------------

start_python2 = time.time()

s = 0
for i in range(100_000_000):
    s += i ** 2

end_python2 = time.time()

print(f"Czysty Python (kwadraty): {end_python2 - start_python2:.4f} sekundy")


# -----------------------------------------
# NumPy
# -----------------------------------------

start_numpy2 = time.time()

x = np.arange(100_000_000)
s = np.sum(x ** 2)

end_numpy2 = time.time()

print(f"NumPy (kwadraty):         {end_numpy2 - start_numpy2:.4f} sekundy")