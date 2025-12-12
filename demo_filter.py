import numpy as np
from belul_fuggveny import pontok_belul
pontok = np.array([[1, 2, 3], [4,5,6], [7,8,9], [10, 10, 10]])
kozep = np.array([4, 5, 6])
hatar = 5
maszk, belul_pontok = pontok_belul(pontok, kozep, hatar)
print("Maszk:", maszk)
print("Határon belüli pontok:")
print(belul_pontok)