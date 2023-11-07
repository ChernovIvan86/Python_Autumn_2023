### Task_19_3
'''
Определите класс Person. При создании объекта
p=Person('Иванов','Иван','Иванович') необходимо
ввести полное имя человека.
при печати print(p) объекта p должно выводится следующее:
# display: вонавИчивонавИнавИ
'''

class Person:
    last_name = None
    first_name = None
    patronymic = None

    def __init__(self, *args):
        self.full_name = args
    def __str__(self):
        return ''.join(self.full_name)[::-1]
print(Person('Иван', 'Иванович', 'Иванов', 'Мусорскай'))
p=Person('Иванов','Иван','Иванович', 'Мусорскай')
print(p.full_name)
print(p.patronymic)
print(dir(p))
print(''.join(p.full_name)[::-1])


