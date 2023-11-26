### Task_29_1
'''
Дан список состоящий из одинаковых чисел
за исключением одного. Найдите это число.
'''
lst = [9,0,0,0,0,0,0,0,0,0,0]
# способ без словаря
for i in range(0, len(lst) - 1):
    if (lst.count(lst[i])) > (lst.count(lst[i + 1])):
        print(f'цифра {lst[i + 1]} встретилась единожды')
    if (lst.count(lst[i])) < (lst.count(lst[i + 1])):
        print(f'цифра {lst[i]} встретилась единожды')

# способ со словарём
lst = [0,0,0,0,0,0,0,0,0,0,9]
dct = dict()
for i in range(0, len(lst)):
    if lst[i] not in dct.keys():
        dct[lst[i]] = 1
    else:
        dct[lst[i]] = dct[lst[i]] + 1

for k, v in dct.items():
    if dct[k] == min(dct.values()):
        print(f'цифра {k} встретилась {v} раз(а)')




