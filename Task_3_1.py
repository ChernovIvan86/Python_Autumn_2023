# Task_3_1
# Bводить в бесконечном цикле зарплаты сотрудников.
# Окончание ввода - ввод 0.
# После чего напечатать среднюю зарплату

from random import randint

n = randint(0, 100)
tes={n}
worker=1

while n != 0:
    n = randint(0, 100)
#    print(n)
    worker += 1
    tes.add(n)

print(sum(tes)/worker)