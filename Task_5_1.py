          # Task_5_1
# Ввести число n. Напечатать треугольник Паскаля
# Например n=4, вывод:
#_____________________
# коэф-ты  |  бином   |
#__________|__________|
#1         | (a+b)**0 |
#1 1       | (a+b)**1 |
#1 2 1     | (a+b)**2 |
#1 3 3 1   | (a+b)**3 |
#1 4 6 4 1 | (a+b)**n |

n = 5

lst = [[1], [1, 1]]
for i in range(2, n+1):
    lst.append([1])
    for k in range(1, i):
        lst[i].append(lst[i - 1][k - 1]+lst[i - 1][k])
    lst[i] += [1]

print(lst)
for i in range(n):
    print(*lst[i])

## Уровень II: запоминать только 2е последние строки.
'''
n = 7
lst_1 = [0, 1]
for i in range(1, n + 1):
    lst_2 = [0]
    for j in range(i):
        lst_2.append(lst_1[j] + lst_1[j + 1])
        print(lst_2[-1], end=' ')
    lst_2.append(0)
    print()
    lst_1 = lst_2.copy()
'''
## Уровень III: запоминать только 2а последних значения.
'''
n = 8
lst = [0, 1, 0]
print(1)
for i in range(2, n + 1):
    x = lst[0]
    for j in range(1, i + 1):
        y = x + lst[j]
        print(y, end=' ')
        x = lst[j]
        lst[j] = y
    print()
    lst.append(0)
'''

