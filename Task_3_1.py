# Task_3_1
# Bводить в бесконечном цикле зарплаты сотрудников.
# Окончание ввода - ввод 0.
# После чего напечатать среднюю зарплату

#from random import randint

dct = dict()
n=1
worker = 1

while worker != '0' or n != 0:
    worker = input('Введите ФИО сотрудника: ')
    if worker == '0': break
    n = int(input('Введите ЕГО зарплату: '))
    if n == 0: break

    if worker in dct.keys():
        dct[worker] += n
    else:
        dct[worker] = n

print(dct)
print(f'Всего работников: {len(dct)}')
print(f'Всего выплачено ЗП: {sum(dct.values())}')
print(f'средняя ЗП: {sum(dct.values())/len(dct)}')

# !!!!!!!!!!!! А без списков, словарей и тд... только с двумя переменными