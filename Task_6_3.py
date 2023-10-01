## Task_6_3.py
# Напишите программу, которая
# 1. принимает на вход строку из смволов.
# 2. Печатает одну строку из букв, вторую из цифр, третью из прочих символов.
# Например: Вход: asd.,sdf=123-234
# Вывод:
# a s d f
# 1 2 3 4
# . , = -
st = 'asd.,sdf=123-234:'
set_alfa = set()
set_numb = set()
set_others = set()

for i in st:
    if i.isalpha(): set_alfa.add(i)
    elif i.isdigit(): set_numb.add(i)
    else: set_others.add(i)

print(*set_alfa)
print(*set_numb)
print(*set_others)