## Task_7_2
# Напишите функцию "def code(string, n)", которая шифрует строку,
# содержащую латинские буквы с помощью шифра Цезаря.
# Каждая буква сдвигается на заданное число n позиций вправо.
# Пробелы и знаки препинания не меняются.
# Например: для n = 1.
# a -> b, b -> c, ..., z -> a
# A -> B, ...
# На выходе функции def code(string, n): печатается сдвинутая строка.
# A-Z - 65-90 (...+32 - строчные); a-z - 97-122
# ord() - ф-я возвращает число — код символа.
# chr() - ф-я возвращает смвол по коду.

st = 'ABZ.abz&'
n = 27

def code(st, n):
    n = n % 26

    st_code = ''
    lst = []

    for i in st:
        lst.append(i)

    for i in range(0, len(lst)):
        num = ord (lst[i])
        if num >= 65 and num <= 90:
            num = num + n
            if num > 90:
                num = num - 26
            lst[i] = chr(num)

    for i in range(0, len(lst)):
        num = ord (lst[i])
        if num >= 65+32 and num <= 90+32:
            num = num + n
            if num > 90 + 32:
                num = num - 26
            lst[i] = chr(num)
    print(lst)
    print(''.join(lst))
    return lst

print(f'было: ', st, '\n','стало: ', ''.join(code(st, n)))
print('!не пойму почему последняя строка отстоит на один пробел!')

