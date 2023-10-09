            # Task_9_3
# Произвести частотный анализ текста из файла.
# 1. С помощью словаря и функции get сосчитать
    # сколько раз встречается каждый символ (без учёта регистра) в тексте.
# 2. Отсортировать по убыванию и напечатать первые 10 символов и их частоты.
     # При равенстве частот отсортировать символы по алфавиту.

x='Adfgj;lg vdfdnd'
from collections import Counter

cont = dict(Counter(x.lower()))
#print(cont.items())
s=sorted(cont.items(), key=lambda x: (x[1],x[0]))
print('s = ', s)

for i in s:
    print(f"'{i[0]}' - {i[1]}")
###########################################
###### С помощью словаря и функции get ####
dct = dict()
for i in x.lower():
    if i in dct.keys():
        dct[i] += 1
    else:
        dct[i] = 1
print(dct)
print(dct == cont)

