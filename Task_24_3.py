## Task_24_3
'''
Создайте функцию, которая принимает на вход строку
из круглых скобок, и возвращает True если строка правильная
(строка не может начинаться с открытой скобки,
а также число открытых и закрытых скобок должны быть равны),
False если строка не правильная.
'''

st = ')()()(())'
#st = '()()(()'
st = '()())(())'

def correct_brackets(str):
    ''''
    :param str:
    :return: bool
    '''
    num_open = 0
    num_closed = 0
    for i in range(0, len(st)):
        if st[i] == ')':
            num_closed += 1
            if num_closed > num_open:
                return False
        if st[i] == '(':
            num_open += 1
    if num_open == num_closed:
        return True
    else:
        return False

print(correct_brackets(st))
