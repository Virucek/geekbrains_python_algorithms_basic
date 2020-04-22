"""
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

import sys

total_mem_1, total_mem_2, total_mem_3 = (0, 0, 0)

# Функция для возвращения памяти элемента:


def obj_mem(x):
    el_mem = 0
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                el_mem += obj_mem(key)
                el_mem += obj_mem(value)
        elif not isinstance(x, str):
            for item in x:
                el_mem += obj_mem(item)
    _mem = sys.getsizeof(x)
    el_mem += _mem
    return el_mem


def sum_mem(*args):
    _total_mem = 0
    for _arg in args:
        _total_mem += obj_mem(_arg)
    return _total_mem


# Непосредственное решение задач

FIRST_SYMBOL = 32
LAST_SYMBOL = 127
STEP = 10

total_mem_const = sum_mem(FIRST_SYMBOL, LAST_SYMBOL, STEP)


# Решение 1a - через рекурсию -- Мне кажется, что я "нечестно" посчитал память в рекурсии, пока не придумал как правильно
# это сделать  -- ПОКА получилось ИТОГ = 650
def str_symb(m, n):
    if m == n:
        return str(m) + "-" + str(chr(m)) + " "
    elif m + STEP < n:
        return str_symb(m, m) + str_symb(m + 1, m + STEP - 1) + "\n" + str_symb(m + STEP, n)
    else:
        return str_symb(m, m) + str_symb(m + 1, n)


res_1a = str_symb(FIRST_SYMBOL, LAST_SYMBOL)
# print(res)
total_mem_1a = sum_mem(res_1a) + total_mem_const

# Решение 1b - через строку и цикл (по сути, заменил рекурсию циклом) | ИТОГ = 1426
total_mem_1_loop_1, total_mem_1_loop_2, total_mem_1_loop_3, total_mem_1_loop_4 = (0, 0, 0, 0)
res_1b = ''
m = FIRST_SYMBOL
while m <= LAST_SYMBOL:
    if m + STEP < LAST_SYMBOL:
        for i in range(m, m + STEP):
            res_1b += str(i) + "-" + chr(i) + " "
            total_mem_1_loop_1 = sum_mem(i, str(i), chr(i))
        res_1b += "\n"
        total_mem_1_loop_2 = sum_mem(range(m, m + STEP))
        m += STEP
    else:
        for i in range(m, LAST_SYMBOL + 1):
            res_1b += str(i) + "-" + chr(i) + " "
            total_mem_1_loop_3 = sum_mem(i, str(i), chr(i))
        total_mem_1_loop_4 = sum_mem(range(m, LAST_SYMBOL))
        m += STEP

total_mem_1b = sum_mem(res_1b) + total_mem_const + total_mem_1_loop_1 + total_mem_1_loop_2 + total_mem_1_loop_3 + total_mem_1_loop_4

# Решение 2 - через матрицу (двумерный массив) | ИТОГ = 8767
start, row = (FIRST_SYMBOL, 0)
res_2 = [[]]
total_mem_2_loop_1, total_mem_2_loop_2, total_mem_2_loop_3, total_mem_row, total_mem_2_loop_4, total_mem_2_loop_5 = (0, 0, 0, 0, 0, 0)
while start + STEP <= LAST_SYMBOL:
    for i in range(STEP):
        _el = str(start + i) + "-" + chr(start + i) + " "
        res_2[row].append(_el)
        total_mem_2_loop_1 = sum_mem(_el, str(start + i), chr(start + i), i)
    start += STEP
    res_2.append(list())
    row += 1
    total_mem_row = sum_mem(range(STEP))
for j in range(start, LAST_SYMBOL + 1):
    _el = str(j) + "-" + str(chr(j))
    res_2[row].append(_el)
    total_mem_2_loop_2 = sum_mem(j, range(start, LAST_SYMBOL + 1), _el)
for r in range(len(res_2)):
    for c in range(len(res_2[r])):
        total_mem_2_loop_3 = sum_mem(c, res_2[r][c])
        #pass
        #print(res_2[r][c], end='\t')
    #print()
    total_mem_2_loop_4 = sum_mem(r, range(len(res_2[r])))
total_mem_2_loop_5 = sum_mem(range(len(res_2)))
total_mem_2 = sum_mem(res_2, start, row) + total_mem_const + total_mem_row + total_mem_2_loop_1 + total_mem_2_loop_2 + total_mem_2_loop_3 + total_mem_2_loop_4 + total_mem_2_loop_5


# Решение 3 - через словарь | ИТОГ = 18474
res_3 = dict()
for k in range(FIRST_SYMBOL, LAST_SYMBOL + 1):
    res_3[k] = chr(k)
    total_mem_3_loop_1 = sum_mem(k, chr(k))
total_mem_3_loop_2 = sum_mem(range(FIRST_SYMBOL, LAST_SYMBOL + 1))
_key = FIRST_SYMBOL
while True:
    if _key + STEP > LAST_SYMBOL:
        for i in range(_key, LAST_SYMBOL + 1):
            total_mem_3_loop_3 = sum_mem(i)
            pass
            #print(f'{str(i)}-{chr(i)}', end='\t')
        total_mem_3_loop_4 = sum_mem(range(_key, LAST_SYMBOL + 1))
        break
    else:
        for i in range(_key, _key + STEP):
            total_mem_3_loop_5 = sum_mem(i)
            pass
            #print(f'{str(i)}-{chr(i)}', end='\t')
        #print()
        total_mem_3_loop_6 = sum_mem(range(_key, _key + STEP))
        _key += 10

total_mem_3 = sum_mem(res_3, _key, range(FIRST_SYMBOL, LAST_SYMBOL + 1), _key) + total_mem_const + total_mem_3_loop_1 + total_mem_3_loop_2 + total_mem_3_loop_3 + total_mem_3_loop_4 + total_mem_3_loop_5 + total_mem_3_loop_6

print(f'{total_mem_1a=}')

print(f'{total_mem_1b=}')

print(f'{total_mem_2=}')

print(f'{total_mem_3=}')

#print(res_1a)
#print(res_1b)
"""
Рекурсия (1a - думаю, это неверный вариант, но на всякий случай) =  650
Через цикл запись результата в строку (1b) = 1426
Запись результата в двумерный массив и вывод через циклы (2) = 8767
Запись результата в словарь и вывод через циклы (3) = 18474

Вывод:
Самым оптимальным по потреблению памяти получились решения 1a и 1b, где результаты записываются в объект строку.
Чем сложнее конструкция, тем менее эффективным получаются решения.
Если исходить из условия задачи просто распечатать список - то решение через строку будет самым оптимальным, но у него
есть и свои проблемы. Если будет необходимо каким-либо образом обработать содержимое таблицы, то это гораздо проще сделать
через список или словарь.

P.S. Сделал через переменные, т.к. договор на уроке был "посчитать" переменные, используемые в цикле, только 1 раз. Если
считать переменные каждый раз, то всё можно сделать через просто переменную total_mem для каждого решения и всё выйдет проще :)

Разрядность ОС - x64
Версия интерпретатора - Python 3.8.2
"""