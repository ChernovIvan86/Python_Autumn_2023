# Task_3_2
# Дано целое число.
# Сосчитать и напечатать сколько в его записи каких цифр.
# Например:
# Вввод:122330.
# Вывод: 0 - 1, 1 - 1, 2 - 2, 3 - 2, 4 - 0 ...

from random import randint

n = randint(1e6, 9e6)
dct = {}
n_st=str(n)
print(n_st)

for i in range(0, 10):
    dct[i] = 0

for i in n_st:
    if int(i) in dct.keys() :
        dct[int(i)]+=1

for k, v in dct.items():
    if dct[k] !=0 :
        print(f'{k} - {dct[k]}')






