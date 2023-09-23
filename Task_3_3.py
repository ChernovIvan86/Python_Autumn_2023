# Task_3_3
# Дано предложение из нескольких слов.
# Слова разделены пробелами.
# Напечатать все самые длинные слова

# Генерация текста
from random import randint

x_b = str()
x_m = str()
x_s = str()
mama_mila_ramu = str()
n = 0

while n != 21:
    x_b = chr(randint(65, 90)) * randint(0, 1)
    x_m = chr(randint(97, 121)) * randint(0, 1)
    x_s = chr(32) * randint(0, 1)
    mama_mila_ramu = mama_mila_ramu + x_b + x_m + x_s
    n += 1
print(mama_mila_ramu)

# Поиск самых длинных слов
lst=[]
lst = mama_mila_ramu.split()
lst.sort(key=len, reverse=True)
print(lst)

print(f'{lst[0]} - {len(lst[0])} символов(а)')
for i in range(1, len(lst)):
    if len(lst[i]) == len(lst[0]):
        print(f'{lst[i]} - {len(lst[i])} символов(а)')



