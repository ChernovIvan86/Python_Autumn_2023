## Task_8_1
# На вход подаётся строка генетического кода,
# состоящая из букв А(Аденин), Г(Гуанин), Ц(Цитозин), Т(Тимн).
# Подкорректируйте код.
# Если рядом стоят А и Г, то поменяйте их местами.
# Если рядом стоят Ц и Т, то поместите АГ междунмим.

st = 'АГЦТГААГГАЦ'
lst = list(st)
lst_sl = []
print(lst)

i = 0
while True:
    if lst[i] == 'А' and lst[i + 1] == 'Г':
        lst[i] = 'Г'
        lst[i + 1] = 'А'
    elif lst[i] == 'Г' and lst[i + 1] == 'А':
        lst[i] = 'А'
        lst[i + 1] = 'Г'
    i += 2
    if i >= len(lst) - 1:
        break
print(lst)

i = 0
while True:
    lst_sl.append(lst[i])
    if (lst[i] == 'Ц' and lst[i + 1] == 'Т') or (lst[i] == 'Т' and lst[i + 1] == 'Ц'):
        lst_sl.append('А')
        lst_sl.append('Г')
        lst_sl.append(lst[i + 1])
    else:
        lst_sl.append(lst[i + 1])
    i += 2
    if i >= len(lst) - 1:
        break
print(lst_sl)