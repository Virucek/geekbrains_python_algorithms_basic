"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
"""

import timeit
import cProfile
#"""
# Не придумал ничего умнее на данный момент, как сразу создавать массив n^2, т.к. функция поиска n-ого простого числа в
# неограниченном решете: p^2 .. + p
# Решение 1 - с помощью алгоритма "Решето Эратосфена"
def sieve(n):
    b = n * n
    res = []
    sieve = [i for i in range(2 + b)]
    sieve[1] = 0
    for i in range(2, 2 + b):
        if sieve[i] != 0:
            j = i + i
            res.append(i)
            if len(res) >= n:
                break
            while j < b:
                sieve[j] = 0
                j += i

    return res[n - 1]

"""
print(timeit.timeit('sieve(150)', number=100, globals=globals())) # 0.5604871
print(timeit.timeit('sieve(300)', number=100, globals=globals())) # 2.4425393
print(timeit.timeit('sieve(450)', number=100, globals=globals())) # 6.383224499999999
print(timeit.timeit('sieve(600)', number=100, globals=globals())) # 11.9879837
print(timeit.timeit('sieve(750)', number=100, globals=globals())) # 19.0116983
print(timeit.timeit('sieve(900)', number=100, globals=globals())) # 28.2934755

cProfile.run('sieve(150)') #        1    0.005    0.005    0.005    0.005 task_2.py:12(sieve)
cProfile.run('sieve(300)') #        1    0.022    0.022    0.026    0.026 task_2.py:12(sieve)
cProfile.run('sieve(450)') #        1    0.050    0.050    0.060    0.060 task_2.py:12(sieve)
cProfile.run('sieve(600)') #        1    0.105    0.105    0.125    0.125 task_2.py:12(sieve)
cProfile.run('sieve(750)') #        1    0.194    0.194    0.239    0.239 task_2.py:12(sieve)
cProfile.run('sieve(900)') #        1    0.247    0.247    0.303    0.303 task_2.py:12(sieve)
"""

# Решение 2 - без использования алгоритма "Решето Эратосфена"
def prime(n):
    res = [2]
    i = 3
    while True:
        flag = 0
        if len(res) >= n:
            break
        for j in res:
            if i % j == 0:
                flag = 1
                break
        if not flag:
            res.append(i)
            i += 1
        i += 1

    return res[n - 1]

#"""
print(timeit.timeit('prime(150)', number=100, globals=globals())) # 0.0788746
print(timeit.timeit('prime(300)', number=100, globals=globals())) # 0.3116499
print(timeit.timeit('prime(450)', number=100, globals=globals())) # 0.6926444999999999
print(timeit.timeit('prime(600)', number=100, globals=globals())) # 1.2471773
print(timeit.timeit('prime(750)', number=100, globals=globals())) # 1.9005290000000001
print(timeit.timeit('prime(900)', number=100, globals=globals())) # 2.7985603

cProfile.run('prime(150)') #        1    0.001    0.001    0.001    0.001 task_2.py:44(prime)
cProfile.run('prime(300)') #        1    0.003    0.003    0.003    0.003 task_2.py:44(prime)
cProfile.run('prime(450)') #        1    0.007    0.007    0.007    0.007 task_2.py:44(prime)
cProfile.run('prime(600)') #        1    0.013    0.013    0.013    0.013 task_2.py:44(prime)
cProfile.run('prime(750)') #        1    0.020    0.020    0.020    0.020 task_2.py:44(prime)
cProfile.run('prime(900)') #        1    0.028    0.028    0.028    0.028 task_2.py:44(prime)
#"""
def test_sieve(func):
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    for i, item in enumerate(lst):
        assert item == func(i + 1)
        print(f'Test {i + 1} OK')

test_sieve(sieve)
test_sieve(prime)

"""
Все решения, кроме 4-го были проверены на N = [150; 900] с шагом 150.
Вывод:
В данной реализации, решение №2 prime работает быстрее и имеет асимптотику O(n^2)
Решение № 1 sieve с использованием решета Эратосфена работает медленнее и имеет асимптотику, близкую к O(n^2 + n).
Проблема решения №1 в выбранной реализации: сразу же создается массив, размерностью n^2. Возможно, можно оптимизировать,
создавая массив из n элементов, затем, если этого недостаточно для того, что найти искомое простое число, добавлять ещё
n элементов в массив.
"""
