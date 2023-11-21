### Task_27_1
'''
Введите одно число n от 1 до 18.
Напечатайте квадратную матрицу, имитирующую мишень Дартс.
Например для n = 5:
11111
12221
12321
12221
11111
'''
import math
n = 4
#n = 5
n = 18
centr = int(math.ceil(n/2))
print(centr)

lst = []
for i in range(n):
    lst.append([])

for i in range(n):
    for j in range(n):
        lst[i].append(1)

count = 0
while True:
    if count == centr:
        break

    # заполнение "2"
    for i in range(0 + count, n - count):
        for j in range(0 + count, n - count):
            lst[i][j] = count + 1
    count += 1

# вывод массива lst
for i in lst:
    print(i)





