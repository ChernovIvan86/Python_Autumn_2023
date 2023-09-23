# Введите список lst, состоящий из чисел.
# Найдите и напечатайте наименьшее число из списка lst.
# Не используйте min, sort, sorted.
from random import randint
lst=[]
dct={}
dct_min={}

'''
for i in range(10):
    lst.append(randint(-10, 10))
'''
lst = [0, 1, 0, 2, 2, 0, 3, 3, 3, 0]
print(lst)

dct={'min':lst[0]}

for i in range(0, len(lst)):
    if lst[i] <= dct['min']: dct['min']=lst[i]
print(*dct, end='')
print(f' in lst = {dct["min"]}')

# Найдите и напечатайте ВСЕ наименьшие числа из списка lst.
for i in range(0, len(lst)):
    if lst[i] == dct['min']: dct_min['index '+str(i)]=lst[i]
print(dct_min)


