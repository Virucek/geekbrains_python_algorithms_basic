"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
"""
import hashlib


def hash_subs_unique(_s):
    hashes = []
    for j in range(1, len(_s) + 1):
        for i in range(j):
            hash_substr = hashlib.sha1(_s[i:j].encode('utf-8')).hexdigest()
            if hash_substr in hashes:
                continue
            else:
                hashes.append(hash_substr)
    return len(hashes) - 1


def test_func(func):
    assert 6 == func("papa")
    print('TEST 1 IS OK')
    assert 9 == func("sova")
    print('TEST 2 IS OK')


test_func(hash_subs_unique)

s = input('Введите строку: ')
print(f'Уникальных подстрок: {hash_subs_unique(s)}')