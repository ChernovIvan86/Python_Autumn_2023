### Task_25_3
'''
Напишите функцию, которая получает
на вход строку из слов, котрые могут
включать буквы верхнего и нижнего регистра,
разделённых пробелами и возвращает строку в CamelStyle.
Пример: camel case word => CamelCaseWord
'''

st = 'camel cAse WorD'
print(''.join(st.title().split()))