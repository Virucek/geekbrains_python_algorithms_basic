"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как коллекция,
элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque

HEX_LIST = list('0123456789ABCDEF')
hex_1 = deque(input(f'Введите 1-ое шестнадцатеричное число: '))
hex_2 = deque(input(f'Введите 2-ое шестнадцатеричное число: '))


def sum_hex(num_1, num_2):
    rest = 0  # Остаток (то, что "держим в уме")
    res_deq = deque([])
    if len(num_2) > len(num_1):  # Заполняем меньшее число нулями слева, чтобы не было ошибки выхода за массив
        num_1.extendleft(list((len(num_2) - len(num_1)) * '0'))
    elif len(num_1) > len(num_2):
        num_2.extendleft(list((len(num_1) - len(num_2)) * '0'))
    for ind in range(len(num_1)):
        ind = (ind + 1) * (-1)
        sum_el = HEX_LIST.index(num_1[ind]) + HEX_LIST.index(num_2[ind]) + rest
        res_deq.appendleft(HEX_LIST[sum_el % len(HEX_LIST)])
        rest = sum_el // len(HEX_LIST)

    return res_deq


def mult_hex(num_1, num_2):
    _total_deq = list()  # Полный список для хранения результатов умножения всех разрядов(Пример:A2 * F, A2 * 4, A2 * C)
    for ind_2 in range(len(num_2)):
        summand = deque()  # Результат хранения каждого разряда (Пример: результат A2 * F)
        rest = 0  # Остаток (то, что "держим в уме")
        _ind_2 = ind_2  # Сохраним значение индекса второго числа перед его изменением
        ind_2 = (ind_2 + 1) * (-1)
        for ind_1 in range(len(num_1)):
            _ind_1 = ind_1
            ind_1 = (ind_1 + 1) * (-1)
            sum_el = HEX_LIST.index(num_1[ind_1]) * HEX_LIST.index(num_2[ind_2]) + rest
            summand.appendleft(HEX_LIST[sum_el % len(HEX_LIST)])
            if _ind_1 + 1 < len(num_1):
                rest = sum_el // len(HEX_LIST)
            else:  # Если всё помножено, а rest ещё остался, его необходимо добавить в очередь слева (даже если 0)
                summand.appendleft(str(sum_el // len(HEX_LIST)))
        if _ind_2 > 0:  # Каждый последующий разряд (после 0) дополняем нулями справа
            summand.extend(list(_ind_2 * '0'))
        _total_deq.append(summand)
    res_deq = _total_deq[0]
    for i in range(1, len(_total_deq)):  # Складываем между собой все результаты умножений разных разрядов
        res_deq = sum_hex(res_deq, _total_deq[i])
    while True:  # Удаляем лидирующие нули :)
        if res_deq[0] != '0':
            break
        res_deq.remove('0')
    return res_deq


def test_sum(func):
    assert deque(['C', 'F', '1']) == func(deque(['A', '2']), deque(['C', '4', 'F']))
    print(f'{func.__name__}: TEST IS OK')


def test_multiple(func):
    assert deque(['7', 'C', '9', 'F', 'E']) == func(deque(['A', '2']), deque(['C', '4', 'F']))
    print(f'{func.__name__}: TEST IS OK')


test_sum(sum_hex)
test_multiple(mult_hex)

print(f'Сумма чисел: {list(sum_hex(hex_1, hex_2))}')
print(f'Произведение чисел: {list(mult_hex(hex_1, hex_2))}')