### Task_26_1
'''
Напишите функцию, которая сравнивает две строки и выдаёт True,
если между ними есть не более чем 1 разница в буквах, и False
во всех остальных случаях. Если две строки равны, то True.
Например:
'abc' и 'abcd' - True,
'acb' и 'abc' - False,
'' и ' ' - False.
'''
st_1 = 'abc'
st_2 = 'abcd'
st_1 = ''
st_2 = ' '
lst_1 = list(st_1)
lst_2 = list(st_2)
lst_res = []
lst_res.append(len(max(st_1, st_2)) - len(min(st_1, st_2)))
for i in range(0, len(min(st_1, st_2))):
    if lst_1[i] == lst_2[i]:
        lst_res.append(0)
    else:
        lst_res.append(1)

if (st_1.isalpha() and st_2.isalpha()) == False:
        print(False)
elif sum(lst_res) > 1:
    print(False)
else:
    print(True)