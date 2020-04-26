"""
 Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
 [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50
array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# uniform вернет вещественное число исключительно правую границу
print(array)
# Описание алгоритма взял из википедии


def merge_sort(arr):
    if len(arr) > 1:
        # Разбиваем массив на две части примерно одинакового размера
        lpart = arr[:len(arr) // 2]
        rpart = arr[len(arr) // 2:]
        # Рекурсивное разбиение задачи на меньшие происходит до тех пор,
        # пока размер массива не достигнет единицы (т.е. до самоупорядоченных массивов).
        merge_sort(lpart)
        merge_sort(rpart)
        # Соединение двух упорядоченных массивов в один.
        l, r, idx = (0, 0, 0)
        while l < len(lpart) or r < len(rpart):
            # Слияние двух подмассивов в третий результирующий. Берем меньший из двух перых элементов подмассивов
            if l < len(lpart) and r < len(rpart):
                if lpart[l] > rpart[r]:
                    arr[idx] = rpart[r]
                    r += 1
                else:
                    arr[idx] = lpart[l]
                    l += 1
            # "Прицепляем" остаток
            elif l < len(lpart):
                arr[idx] = lpart[l]
                l += 1
            else:
                arr[idx] = rpart[r]
                r += 1
            idx += 1


merge_sort(array)
print(array)