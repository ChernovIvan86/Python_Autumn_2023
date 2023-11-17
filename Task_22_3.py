### Task_22_3
'''
Существуют ключевые слова, которые нельзя использовать
для названия переменных, функций и классов. Для получения
списка всех ключевых слов можно воспользоваться атрибутом
kwlist из модуля keyword.
Напишите программу, которая принимает строку текста
и заменяет в ней все ключивые слова на <kw>.
'''

import keyword
print(keyword.kwlist)

st = 'Fals False None True and as assert'
lst = st.split()
for i in range(0, len(lst)):
    if lst[i] in keyword.kwlist:
        lst[i] = '<kw>'
print(' '.join(lst))



