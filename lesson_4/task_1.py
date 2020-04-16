"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import random
import timeit
import cProfile

def gen_array(size):
    MIN_ITEM = -100_000
    MAX_ITEM = 100_000
    return [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]

# Решение 1 - через 1 цикл c 2 условиями без использования временных переменных
def func(array):
    min_ind_1, min_ind_2 = (0, 1) if array[0] < array[1] else (1, 0)
    for j in range(1, len(array)):
        if array[min_ind_1] > array[j]:
            min_ind_1, min_ind_2 = j, min_ind_1
        elif array[min_ind_2] > array[j]:
            min_ind_2 = j
    return array[min_ind_1], min_ind_1, array[min_ind_2], min_ind_2

"""
size = 1_000_000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
print(timeit.timeit('func(array)', number=100, globals=globals())) # 16.6017519
cProfile.run('func(array)') # 1    0.165    0.165    0.165    0.165 task_1.py:14(func)

size = 1_500_000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
print(timeit.timeit('func(array)', number=100, globals=globals())) # 25.529696299999998
cProfile.run('func(array)') # 1    0.259    0.259    0.259    0.259 task_1.py:14(func)

size = 2_000_000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
print(timeit.timeit('func(array)', number=100, globals=globals())) # 34.094698699999995
cProfile.run('func(array)') # 1    0.333    0.333    0.333    0.333 task_1.py:14(func)

size = 2_500_000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
print(timeit.timeit('func(array)', number=100, globals=globals())) # 42.29647490000001
cProfile.run('func(array)') # 1    0.419    0.419    0.419    0.419 task_1.py:14(func)

size = 3_000_000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
print(timeit.timeit('func(array)', number=100, globals=globals())) # 54.62562939999998
cProfile.run('func(array)') # 1    0.502    0.502    0.502    0.502 task_1.py:14(func)
"""


# Решение 2 - через 1 цикл c 2 условиями С использованием временных переменных min_2 и min_1
def func_2(array):
    min_ind_1, min_ind_2 = (0, 1) if array[0] < array[1] else (1, 0)
    min_1, min_2 = (array[min_ind_1], array[min_ind_2])
    for j in range(1, len(array)):
        if min_1 > array[j]:
            min_ind_1, min_ind_2 = j, min_ind_1
            min_1, min_2 = array[j], min_1
        elif min_2 > array[j]:
            min_ind_2 = j
            min_2 = array[j]
    return min_1, min_ind_1, min_2, min_ind_2

"""
array = gen_array(1_000_000)
print(timeit.timeit('func_2(array)', number=100, globals=globals())) # 10.560668
cProfile.run('func_2(array)') # 1    0.110    0.110    0.110    0.110 task_1.py:54(func_2)

array = gen_array(1_500_000)
print(timeit.timeit('func_2(array)', number=100, globals=globals())) # 16.0251503
cProfile.run('func_2(array)') # 1    0.157    0.157    0.157    0.157 task_1.py:54(func_2)

array = gen_array(2_000_000)
print(timeit.timeit('func_2(array)', number=100, globals=globals())) # 21.0980019
cProfile.run('func_2(array)') # 1    0.208    0.208    0.208    0.208 task_1.py:54(func_2)

array = gen_array(2_500_000)
print(timeit.timeit('func_2(array)', number=100, globals=globals())) # 26.60853970000001
cProfile.run('func_2(array)') # 1    0.261    0.261    0.261    0.261 task_1.py:54(func_2)

array = gen_array(3_000_000)
print(timeit.timeit('func_2(array)', number=100, globals=globals())) # 33.33949109999999
cProfile.run('func_2(array)') # 1    0.312    0.312    0.312    0.312 task_1.py:54(func_2)

"""


# Решение 3 - через 2 цикла
def func_3(array):
    min_ind_1, min_ind_2 = (0, 1) if array[0] < array[1] else (1, 0)
    for j in range(1, len(array)):
        if array[min_ind_1] > array[j]:
            min_ind_1, min_ind_2 = j, min_ind_1

    for i in range(min_ind_1 + 1, len(array)):
        if array[min_ind_2] > array[i]:
            min_ind_2 = i

    return array[min_ind_1], min_ind_1, array[min_ind_2], min_ind_2
"""
array = gen_array(1_000_000)
print(timeit.timeit('func_3(array)', number=100, globals=globals())) # 16.3657104
cProfile.run('func_3(array)') # 1    0.164    0.164    0.164    0.164 task_1.py:91(func_3)

array = gen_array(1_500_000)
print(timeit.timeit('func_3(array)', number=100, globals=globals())) # 24.3140307
cProfile.run('func_3(array)') # 1    0.243    0.243    0.243    0.243 task_1.py:91(func_3)

array = gen_array(2_000_000)
print(timeit.timeit('func_3(array)', number=100, globals=globals())) # 31.742031499999996
cProfile.run('func_3(array)') # 1    0.312    0.312    0.312    0.312 task_1.py:91(func_3)

array = gen_array(2_500_000)
print(timeit.timeit('func_3(array)', number=100, globals=globals())) # 38.4796145
cProfile.run('func_3(array)') # 1    0.371    0.371    0.371    0.371 task_1.py:91(func_3)

array = gen_array(3_000_000)
print(timeit.timeit('func_3(array)', number=100, globals=globals())) # 50.45658830000001
cProfile.run('func_3(array)') # 1    0.505    0.505    0.505    0.505 task_1.py:91(func_3)

"""
# Решение 4 - искусственное, через рекурсию, просто так.
# Т.к. это извращение работает крайне медленно, замеры проводились на малых массивах
def func_4(array):
    min_1, min_2, start_idx = (0, 0, 0)
    def _func_4(start_ind, array):
        if (len(array) - start_ind) == 1:
            return array[0]
        elif (len(array) - start_ind) == 2:
            return array[start_ind] if array[start_ind] < array[-1] else array[-1]
        else:
            return array[start_ind] if array[start_ind] < _func_4(start_ind + 1, array) else _func_4(start_ind + 1, array)

    min_1 = _func_4(start_idx, array)
    spam_lst = array.copy()
    spam_lst.remove(min_1)
    min_2 = _func_4(start_idx, spam_lst)
    if spam_lst.index(min_2) >= array.index(min_1):
        return min_1, array.index(min_1), min_2, spam_lst.index(min_2) + 1
    else:
        return min_1, array.index(min_1), min_2, spam_lst.index(min_2)

#"""
array = gen_array(10)
print(timeit.timeit('func_4(array)', number=100, globals=globals())) # 0.0217073
cProfile.run('func_4(array)')
#         1    0.000    0.000    0.000    0.000 task_1.py:126(func_4)
#     594/2    0.000    0.000    0.000    0.000 task_1.py:128(_func_4)

array = gen_array(15)
print(timeit.timeit('func_4(array)', number=100, globals=globals())) # 0.3222161
cProfile.run('func_4(array)')
#         1    0.000    0.000    0.007    0.007 task_1.py:126(func_4)
#    9262/2    0.006    0.000    0.007    0.003 task_1.py:128(_func_4)

array = gen_array(20)
print(timeit.timeit('func_4(array)', number=100, globals=globals())) # 5.4903424
cProfile.run('func_4(array)')
#         1    0.000    0.000    0.114    0.114 task_1.py:126(func_4)
#  151551/2    0.097    0.000    0.114    0.057 task_1.py:128(_func_4)

array = gen_array(25)
print(timeit.timeit('func_4(array)', number=100, globals=globals())) # 50.0825126
cProfile.run('func_4(array)')
#         1    0.000    0.000    1.084    1.084 task_1.py:126(func_4)
# 1380382/2    0.921    0.000    1.084    0.542 task_1.py:128(_func_4)

array = gen_array(26)
print(timeit.timeit('func_4(array)', number=100, globals=globals())) # 187.8498208
cProfile.run('func_4(array)')
#         1    0.001    0.001    3.982    3.982 task_1.py:126(func_4)
# 5275903/2    3.374    0.000    3.981    1.991 task_1.py:128(_func_4)

#"""


def test_find_2_min(func):
    lst = [-100, 95, -35, 17, 11, -13, 117, -59, 23, 0, -2, 3, 87, -39, -23]
    assert func(lst) == (-100, 0, -59, 7)
    print(f'{func.__name__}: Test 1 is OK')
    lst = [-1, 95, -35, 17, 11, -13, -117, -9, 23, 0, -2, 3, 87, -117, -23]
    assert func(lst) == (-117, 6, -117, 13)
    print(f'{func.__name__}: Test 2 is OK')
    lst = [11, 95, 35, 17, 11, 13, 117, 9, 23, 10, 2, 3, 87, 117, -23]
    assert func(lst) == (-23, 14, 2, 10)
    print(f'{func.__name__}: Test 3 is OK')
    lst = [112, 115, 90, 170, 116, 1339, 1170, 35, 233, 101, 2867, 305, 870, 117, 223]
    assert func(lst) == (35, 7, 90, 2)
    print(f'{func.__name__}: Test 4 is OK')


test_find_2_min(func)
test_find_2_min(func_2)
test_find_2_min(func_3)
test_find_2_min(func_4)

"""
Все решения, кроме 4-го были проверены на N = [1_000_000; 3_000_000] с шагом 500_000.
Вывод:
По результатам замеров, оказалось, что решение №2 (с одним циклом и временными переменными для хранения значений min_1
и min_2) является самым быстрым, сложность в нем - O(n) (линейная);
Решение 1 также имеет линейную сложность O(n), т.к. проходим один массив, но постоянно пересчитывая array[i] тратится 
доп. время (мое предположение);
Решение 2 по сути более оптимизированная версия решения 1 с использованием меморизации (проходит быстрее и с меньшим 
количеством памяти);
Решение 3 по сути имеет линейную сложность. 
Хотя по идее должен иметь сложность O(n ^ 2) - т.к. по сути прогоняются 2 массива, но по замерам и времени и памяти 
этого не скажешь, т.к. он почти не отличается от результатов решения № 1, хотя увеличив N ещё, кажется, что зависимость
 начала проявляться;
Решение 4 - просто эксперимент  :) массив из 30 элементов обрабатывается больше нескольких часов. Имеет асимптотику,
 близку к O(n^5) или O(2^n).
"""