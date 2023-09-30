
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

# создание списка lst из неглубоких копий спискаспискоа lst_0
count = 0
while count != n:
    lst.append(lst_0.copy())
    count += 1

## вычисление необходимого числа шагов
# для заполнения массива размерностью n*n
sum_steps = n * 2 - 1
print(sum_steps)

## первый шаг заполнения спирали
for i in range(0, n):
    lst[0][i] = i+1

akt_steps = n + 1
a = 0
while akt_steps != sum_steps:

    for i in range(1, n):

        lst[i][n - 1] = akt_steps
        akt_steps += 1


    a += (math.pi / 2)



    if akt_steps != sum_steps: break
'''
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


for i in lst:
    print(i)


dct = dict()
for i in range(n+1, n*n+1):
    dct[i] = (0, 0)
print(dct)