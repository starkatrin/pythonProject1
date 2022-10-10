import numpy as np
from random import randint

n = int(input('Введите количество строк:'))
m = int(input('Введите количество столбцов:'))
array = [[randint(1, 10) for i in range(m)] for j in range(n)]
print(array)

array = (sorted([m for n in array for m in n]))

new_array = [array[i:i+m] for i in range(0, len(array), m)]
print(array, new_array, sep ='\n')
