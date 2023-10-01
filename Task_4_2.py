## Task_4_2
# Ввод: натуральное число n/
# Вывод: спираль из чисел от 1 до n
# Например: n = 4:
#  1  2  3  4
#  12 13 14 5
#  11 16 15 6
#  10  9  8 7
#

import math
#n = int(input('Введите n >= 2: '))
n = 4

## создание списка lst списков lst_0, размерностью n*n
lst_0 = []
lst = []
count = 0

# создание списка lst_0
while count != n:
    lst_0.append([])
    count += 1

# создание списка lst из неглубоких копий списка lst_0
count = 0
while count != n:
    lst.append(lst_0.copy())
    count += 1

## вычисление необходимого числа шагов
# для заполнения массива размерностью n*n
sum_steps = n ** 2
print(sum_steps)

'''
## первый шаг заполнения спирали
for i in range(0, n):
    lst[0][i] = i+1
print(f'cos(0) = {round(math.cos(0))}')
print(f'cos(pi/2) = {round(math.cos(math.pi / 2))}')
print(f'cos(pi) = {round(math.cos(math.pi))}')
print(f'cos(pi*3/2) = {round(math.cos(math.pi * 3 / 2))}')
print(f'cos(2*pi) = {round(math.cos(math.pi * 2))}')

print(f'sin(0) = {round(math.sin(0))}')
print(f'sin(pi/2) = {round(math.sin(math.pi / 2))}')
print(f'sin(pi) = {round(math.sin(math.pi))}')
print(f'sin(pi*3/2) = {round(math.sin(math.pi * 3 / 2))}')
print(f'sin(2*pi) = {round(math.sin(math.pi * 2))}')
a = 0
while True:
    print(f'sin({a}) = {round(math.sin(a))}')
    a += (math.pi / 2)
    input()
'''

for i in range(0, n - 1):
    if i < n:
        for j in range(0, len(lst[i])):
            lst[i][j] = j + 1




for i in lst:
    print(i)
