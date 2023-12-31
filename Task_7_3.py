## Task_7_3
# Дан двумерный массив x чисел в виде списка,
# содержащего строки в виде списков.
# Размер массива n - строк и m - столбцов.
# Напишите функцию,
# которая принимает этот массив как аргумент
# и выдаёт отсортированный список из трёх самых больших чисел.
# Например:
# Ввод: n = 2, m = 3, x = [[1, 6, 3], [4, 5, 4]]
# Вывод: [4, 5, 6]

def sor_3(x,m):

    tes = set()

    for i in range(0, len(x)):
        for j in range(0, m):
            tes.add(x[i][j])

    lst = list(tes)
    lst.sort(reverse=True)

    lst_max_3 = []
    for i in range(0, 3):
        lst_max_3.append(lst[i])
    print(sorted(lst_max_3))

n, m = 2, 3
x = [[1, 6, 3], [4, 5, 4]]

sor_3(x, m)


# Контрольный вариант Task_7_3
lst = [[1, 6, 3], [4, 5, 4]]
cmn = []
for i in lst:
    cmn.extend(i)
print(sorted(cmn)[-3:])
