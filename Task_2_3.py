# Введите число n.
# Сосчитайте и напечатайте факториал числа n.
# Не используйте функцию math.factorial().

from random import randint
from math import factorial
count=1
n=randint(1, 10)
if n==1: print(n,'!=',n)
else:
    for i in range(1, n+1):
        count*=i
print(f'{n}!={count}')
print(f'math.factorial({n})= {factorial(n)}')
#
#
