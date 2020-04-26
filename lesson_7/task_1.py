"""
. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
[-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные версии
сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""
import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randrange(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]  # randrange - исключает правое значение [-100; 100)
print(array)


def bubble_sort(arr):
    n = 1
    # На самом деле, прогонять массив полностью n, где n -> len(arr) - 1 не имеет смысла, т.к. гарантированно массив
    # будет отсортирован за n = len(arr) - 2 прогонов
    # например, если в массиве 10 элементов, массив упорядочится уже за 9 прогонов.
    while n < len(arr) - 1:
        flag = 0
        # Будем считать, что справа n элементов уже отсортированы, а значит, следует проверять только неотсортированную
        # часть
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                flag = 1
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            # print(i, arr[i])
        if flag == 0:  # Если вдруг массив отсортирован уже на прогоне, меньшем, чем n, то перестаем его гонять по циклу
            break
        n += 1


bubble_sort(array)
print(array)

