"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

NUMS_SIZE = 8

MIN_NUM = 2
MAX_NUM = 9

MIN_NAT_NUM = 2
MAX_NAT_NUM = 99

res = [0 for i in range(NUMS_SIZE)]
nums = range(MIN_NUM, MAX_NUM + 1)

for i in range(MIN_NAT_NUM, MAX_NAT_NUM + 1):
    for m in nums:
        if i % m == 0:
            res[m - 2] += 1

for i in range(NUMS_SIZE):
    print(f'{nums[i]} - {res[i]}')
