"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import random

SIZE = 1_000_000
MIN_ITEM = -100_000_000
MAX_ITEM = 100_000_000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# Решение 1
min_1, min_2, min_ind_1, min_ind_2 = 0, 0, 0, 0
for j in range(len(array)):
    if min_1 > array[j]:
        min_1, min_2 = array[j], min_1
        min_ind_1, min_ind_2 = j, min_ind_1
    elif min_2 > array[j]:
        min_2 = array[j]
        min_ind_2 = j

print(f'Первое решение:\n{min_1=}\n{min_ind_1=}\n{min_2=}\n{min_ind_2=}\n')

# Решение 2 -- на миллионе записей работает приблизительно такое же время, что и решение 1
min_1, min_2, min_ind_1, min_ind_2 = 0, 0, 0, 0
for j in range(len(array)):
    if min_1 > array[j]:
        min_1, min_2 = array[j], min_1
        min_ind_1, min_ind_2 = j, min_ind_1

for i in range(min_ind_1 + 1, len(array)):
    if min_2 > array [i]:
        min_2 = array[i]
        min_ind_2 = i
print(f'Второе решение:\n{min_1=}\n{min_ind_1=}\n{min_2=}\n{min_ind_2=}')