###Task_16_1
# Напишите функцию, которая использует RE.
# На вход подаётся строка, например,
# "Институт точной механики оптики".
# Функция создаёт сокращение "ИТМО"
#
# Работа над ошибками
########
import re
def fun(x):
    a = x.group().upper()[0]
    return a

st = 'Институт точной механики оптики'
res_1 = re.sub(r'\b\w+\b', fun, st)

print(res_1.replace(' ', ''))






