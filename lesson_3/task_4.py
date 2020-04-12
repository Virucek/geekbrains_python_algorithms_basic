"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

import random

SIZE = 1_000_000
MIN_ITEM = -100_000_000
MAX_ITEM = 100_000_000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# Сперва найдем первое отрицательное число в списке
max_neg, max_neg_ind = 0, 0
# -- вариант, если мы точно знаем, что есть отрицательный элемент
while array[max_neg_ind] >= 0:
    max_neg_ind += 1
max_neg = array[max_neg_ind]

#max_neg, max_neg_ind = 0, -1 -- если -1, то отрицательные элементы отсутствуют.
#for i in range(len(array)):
#    if array[i] < 0:
#        max_neg = array[i]
#        max_neg_ind = i
#        break

for j in range(max_neg_ind + 1, len(array)):
    if array[j] < 0 and array[j] > max_neg:
        max_neg = array[j]
        max_neg_ind = j

print(f'Максимальный отрицательный элемент: {max_neg} \nИндекс максимального отрицательного элемента: {max_neg_ind}')