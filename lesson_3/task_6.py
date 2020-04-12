"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

ROW_NUMS = 5
COLUMN_NUMS = 4
matrix = []

for i in range(ROW_NUMS):
    column = []
    sum_column = 0
    for j in range(COLUMN_NUMS - 1):
        el = int(input(f'Введите элемент №{j + 1} в строку №{i + 1}: '))
        sum_column += el
        column.append(el)
    column.append(sum_column)
    matrix.append(column)

for row in matrix:
    for _, el in enumerate(row):
        print(f'{el:>5}', end='')
    print()