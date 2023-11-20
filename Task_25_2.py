### Task_25_2
'''
Реализуйте функцию is_palindrome() с использованием рекурсии,
которая принимает один аргумент str - произвольная строка.
Возвращает значение True, если переданная строка является палиндромом,
или False в противном случае.
Палиндромом является строка одинаково читающаяся в обоих направлениях
(пустая строка и строка из одного символа являются палиндромами).
'''
st = ''
st = ' '
st = 'a'
st = 'abcddcba'
#st = 'abra'
def is_palindrome(st):
    if len(st) < 1:
        return True
    else:
        if st[0] == st[-1]:
            return is_palindrome(st[1:-1])
        else:
            return False
#a = str(input("Введите строку:"))
a = st
print(is_palindrome(a) == True)



