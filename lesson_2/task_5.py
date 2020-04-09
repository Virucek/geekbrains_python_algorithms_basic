"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


def sum(n):
    if n // 10 == 0:
        return n
    else:
        return n % 10 + sum(n // 10)


s, max, num = 0, 0, 0
while True:
    a = int(input('Введите натуральное число, для выхода введите 0: '))
    if a == 0:
        print(f'Число = {num}, сумма его цифр = {max}')
        break
    else:
        s = sum(a)
        if s > max:
            max, num = s, a