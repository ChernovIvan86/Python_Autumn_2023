### Task_26_3
'''
Создайте класс Person, определите в нём атрибут self._age
используйте декоратор @property для определения методов
getter, setter, deleter.
В методе setter определите проверку, что возраст не может быть
меньше 1 и больше 100. При попытке установить этот возраст
программа должна напечатать "Недоступный возраст".
'''


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if (age > 1) and (age < 100):
            self._age = age
        else:
            print("Недоступный возраст")



p = Person('Agy', 101)
p.age = 0
#print(p._age())

