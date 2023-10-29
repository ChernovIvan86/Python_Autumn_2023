    ### Task_18

# Разработать систему решения задач учениками курса
# «Разработчик на Питоне и проверке их преподавателем.
    # 1. Преподаватель каждый урок задает некоторое количество задач
    # в качестве домашнего задания, для упрощения можно считать что одну.
    # Посылает их каждому ученику.
    # 2. Каждый ученик решает каждую задачу, переводит её статус
    # в решённую и посылает решение преподавателю.
    # 3. Преподаватель проверяет каждую задачу каждого ученика
    # и подтверждает её статус как решённую или меняет её статус
    # на нерешённую и посылает результат ученику.

# Разработайте систему классов (Teachers, Pupils).
# Можно создать другие классы, например Tasks.
# Разработайте систему атрибутов для каждого класса
# для хранения и использования описанных процессов.
# Проверьте её работу на одном учителе и 2-3, учениках.


meta_data = {0: True, 1: True, 2: True, 3: True, 4: True, 5: True}
task_registry = dict()
name_list = dict()
class ITMO:
    name = 'no_name'
    intelligence = 'no_intelligence'
    level = 1
class Teachers(ITMO):
    intelligence = meta_data
    level = 'archmage'
    def push_task(self, x):
        """ Функция выдачи задания"""
        task_data = {}
        for k, v in enumerate(meta_data):
            task_data[v] = None
            x.intelligence = task_data

    def checking_tasks(self, stud):
        """ Функция проверки задания и перевода
        студента на следующий курс"""
        if stud.intelligence == meta_data:
                stud.level += 1
                print(stud, stud.name, ' level = ', stud.level)





class Pupils(ITMO):
    def solve_the_task(self, z):
        """ Функция решения задания и его отправки"""
        for k, v in enumerate(z.intelligence):
            z.intelligence[v] = True
        task_registry[z.name] = z.intelligence


# В ИТМО устроился учитель 'Mariya_Iv'
Teacher_1 = Teachers()
Teacher_1.name = 'Mariya_Iv'
print(Teacher_1.name, Teacher_1.intelligence, 'level= ', Teacher_1.level)

# В ИТМО зачислен студент 'Vovochka'
a = Pupils()
a.name = 'Vovochka'
name_list[a.name] = a
print(a.name, a.intelligence, 'level= ', a.level)
print('name_list = ', name_list)

# "Teacher_1" отправил задание ученику "a".
Teacher_1.push_task(a)
print(a.name, a.intelligence)

# "ученик "a" решил своё задание и отправил его.
a.solve_the_task(a)
print(a.name, a.intelligence)
print('task_registry = ', task_registry)

# "Teacher_1" проверил задание у ученика "а"
# и если он справился, то перевёл его на следующий курс.
Teacher_1.checking_tasks(a)
print(a.name, a.intelligence, a.level)

# ????? не смог заставить учителя проверить решение задания у 'Vovochka'
    # в реестре решёных заданий 'task_registry',
    # поэтому проверял непосредственно у 'Vovochka' в a.intelligence.
