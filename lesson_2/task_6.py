"""
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


def str_symb(m, n):
    if m == n:
        return str(m) + "-" + str(chr(m)) + " "
    elif m + 10 < n:
        return str_symb(m, m) + str_symb(m + 1, m + 9) + "\n" + str_symb(m + 10, n)
    else:
        return str_symb(m, m) + str_symb(m + 1, n)


FIRST_SYMBOL = 32
LAST_SYMBOL = 127
res = ""

res = str_symb(FIRST_SYMBOL, LAST_SYMBOL)
print(res)