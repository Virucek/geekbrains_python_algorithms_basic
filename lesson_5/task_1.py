"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
редприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.
"""

from collections import Counter

QUARTERS = 4
comp_counter = Counter()

comp_nums = int(input('Укажите количество предприятий: '))
for i in range(comp_nums):
    comp_name = input(f'Введите наименование предприятия {i + 1}: ')
    for j in range(QUARTERS):
        comp_counter[comp_name] += int(input(f'Укажите прибыль предприятия {comp_name} за {j + 1} квартал: '))

profit_avg = sum(comp_counter.values()) / comp_nums

lst_above, lst_below = ([], [])
for k in comp_counter:
    if comp_counter[k] >= profit_avg:
        lst_above.append(k)
    else:
        lst_below.append(k)
# 'Компаний с низкой прибылью нет' - вариант, если у всех предприятий была одинаковая прибыль.
print(f'Средняя прибыль = {profit_avg:.2f}',
      f'Компании, чья прибыль выше или равна средней: {lst_above}',
      f'Компании, чья прибыль ниже среднего: {lst_below}' if len(lst_below) > 0 else f'Компаний с низкой прибылью нет',
      sep='\n')

