## Task_5_2
# Ввести число и напечатать все его делители.
# Например: Ввод: 12; Вывод: 1 2 3 4 6 12.
# Усложнённый вариант: напечатать только
# простые делители и их степени.
#
from math import inf
n = 12
# Вычисление всех делителей числа n.
for i in range(1, n + 1):
    if n % i == 0: print(i, end=' ')

# запись всех делителей в словарь
dct = dict()
dct_prime = dict()
for i in range(2, n + 1):
    if n % i == 0:
        dct[i] = 1
# print()
# print(dct)

## выбор простых делителей
# замена числа вхождений НЕпростого ключа на inf
for i in range(3, n+1):
    for j in range(2, i):
        if i % j == 0 and i in dct.keys():
            dct[i] = inf

# заполнение второго словаря простыми ключами
for i in dct.keys():
    if dct[i] != inf:
        dct_prime[i] = dct[i]
# print()
# print(dct_prime)

# вычисление степеней простых делителей
for i in dct_prime.keys():
    chas = n / i
    while chas % i == 0:
        chas = chas / i
        dct_prime[i] += 1
print()
print(dct_prime)
for k, v in dct_prime.items():
    print(f'{k} - {v}')


