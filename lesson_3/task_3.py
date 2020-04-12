"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

SIZE = 1_000_000
MIN_ITEM = -100_000_000
MAX_ITEM = 100_000_000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_ind, max_ind = 0, 0
max, min = array[0], array[0]
for i in range(1, len(array)):
    if array[i] > max:
        max = array[i]
        max_ind = i
    elif min > array[i]:
        min = array[i]
        min_ind = i
array[min_ind], array[max_ind] = array[max_ind], array[min_ind]

print(f'Индекс минимального элемента - {min_ind} \nИндекс максимального - {max_ind} \nИзмененный список: {array}')

