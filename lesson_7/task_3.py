"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
в другой — не больше медианы.
"""

import random

SIZE = 5
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(2 * SIZE + 1)]
print(array)


# Решение № 1 (без сортировки)
def find_med(arr):
    med_idx = 0

    def _find_med(arr, _med_idx):
        _r = _l = 0
        _arr = arr.copy()
        _med = _arr.pop(_med_idx)
        for i in range(len(_arr)):
            if _arr[i] > _med:
                _r += 1
            elif _arr[i] < _med:
                _l += 1
            # Если у нас есть четное количество одинаковых элементов в массиве, надо определить рассматриваемый элемент
            # правее или левее _med_idx (Иначе считать количество элементов "не больше" и "не меньше" будем неверно)
            elif i >= _med_idx:
                _r += 1
            else:
                _l += 1
        return _r, _l

    r, l = _find_med(arr, med_idx)
    while r != l:  # Выхода за массив здесь быть не может, поэтому добавлять проверку не стал.
        med_idx += 1
        r, l = _find_med(arr, med_idx)
    return arr[med_idx]


# Решение № 2 (используя неоптимизированную гномью сортировку)
def find_med_gnome(arr):

    def gnome_sort(_arr):
        i = 1
        while i < len(_arr):
            # Сравниваем с предыдущим элементом. Если всё ок - двигаемся дальше
            if _arr[i - 1] <= _arr[i]:
                i += 1
            else:  # Если не ок, меняем эл-ты местами, идем назад (если есть куда) и перепроверяем снова
                _arr[i - 1], _arr[i] = _arr[i], _arr[i - 1]
                if i > 1:
                    i -= 1
                # i-= 1
                # if i == 0:
                #   i += 1

    gnome_sort(arr)
    med_idx = len(arr) // 2
    return arr[med_idx]


# Решение № 3 (используя оптимизированную гномью сортировку. Сначала написал, потом уже увидел ошибку в решении №2, но
# всё равно оставил ещё и это решение :)
def find_med_gnome_opt(arr):
# pos содержит позицию, в которой был гном, пока не пошел влево по массиву (случайно увидел в интернете идею и уже не
# смог развидеть) - помогает избежать лишних итераций и сравнений
    def gnome_sort(_arr):
        i, pos = (1, 2)
        while i < len(_arr):
            if _arr[i - 1] < _arr[i]:
                i = pos
                pos += 1
            else:
                _arr[i - 1], _arr[i] = _arr[i], _arr[i - 1]
                if i > 1:
                    i -= 1
                else:  # Если идти больше некуда, возвращаемся в прежнюю позицию, которая содержится в pos
                    i = pos
                    pos += 1

    gnome_sort(arr)
    med_idx = len(arr) // 2
    return arr[med_idx]


print(f'Медиана (без сортировки): {find_med(array)}')
print(f'Медиана (неоптимизированная гномья сортировка): {find_med_gnome(array.copy())}')
print(f'Медиана (оптимизированная гномья сортировка): {find_med_gnome_opt(array.copy())}')# copy, чтобы оригинальный array не менять
