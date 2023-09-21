def Mult2(a):
    return a*2

print('Hello world!')
print("Привет мир!")

st='Hello world!'
lst=st.split()
print(lst)


#lst=['1', 2, 2, 'e', '8']
i=list(map(Mult2, lst))
print("L2 = ", i)

lst=list(st)
print(lst)
i=list(map(Mult2, lst))
print("L2 = ", i)

i=list(map(lambda x: x*2, lst))
print("L2 = ", i)

# форматирование

l=st.split()
print(st, f'и Серёжа то же: {l[0]} !!!')
#print(st, f'и Серёжа то же: {} !!!')


# напишите программу, которая принимает три имени
# и печатает их через ':' в обратном порядке
a='Анна'
b='Василий'
c='Алёша'
lst=[a, b, c]
lst.reverse()
st = ":".join(lst)
print(*lst)
print(st)
##################################################
# введите число, вывести оно больше нуля или меньше
x = -8
print(f'{x} больше 0') if x > 0 else (print(f'{x} меньше 0') if x < 0 else print(f'{x} есть 0'))

#напечатайте большее из двух чисел
x = 6
y = -9
print(max(x, y))

