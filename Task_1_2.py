            # Task_1_1,2,3
# ввести числа x и y.Напечатать наибольшее из чисел x+y,x-y, x*y, x/y, x//y)
#x=float(input('ВВЕДИТЕ X:'))
#y=float(input('ВВЕДИТЕ Y:'))

##### I-й вариант
x, y = 2, 2
if y==0: print('y=' ,y,' на НУЛЬ делить НЕльзя! Попробуйте ещё')

dct = {'x+y=': x+y,
       'x*y=': x*y,
       'x-y=': x-y,
       'x/y=': x/y,
       'x//y=': x//y}

min_1_dct = dct.get( min(dct, key=dct.get))
max_1_dct = dct.get( max(dct, key=dct.get))
print(f'минимальное значение {min_1_dct}, максимальное значение {max_1_dct}')

## ПОИСК первых МАКСИМАЛЬНых значений и их замена на минимальное
for k, v in dct.items():
    if v == max_1_dct:
        dct[k]=min_1_dct

## ПОИСК второго по величине значения и его печать
max_2_dct = dct.get( max(dct, key=dct.get))
print(f'второе по величине значение {max_2_dct}')

##### II-й вариант
x, y = 2, 2
if y==0: print('y=' ,y,' на НУЛЬ делить НЕльзя! Попробуйте ещё')

dct = {'x+y=': x+y,
       'x*y=': x*y,
       'x-y=': x-y,
       'x/y=': x/y,
       'x//y=': x//y}
# метод .items() возвращает итерируемый объект.
# Такой объект содержит пары ключ-значение для словаря по аналогии с кортежами в списке

## ПОИСК МИНИМАЛЬНОГО значения
min_1_dct = dct.get('x+y=')
for k, v in dct.items():
    if min_1_dct > dct.get(k): min_1_dct = dct.get(k)

# ПОИСК МАКСИМАЛЬНОГО значения
max_1_dct = dct.get('x+y=')
for k, v in dct.items():
    if v > max_1_dct: max_1_dct = v

## ПОИСК первого МАКСИМАЛЬНОГО значения, печать и его замена на минимальное
for k, v in dct.items():
    if v == max_1_dct:
        print(f'наибольший результат {k, v}')
        dct[k]=min_1_dct

# ПОИСК второго МАКСИМАЛЬНОГО значения
max_2_dct = dct.get('x+y=')
for k, v in dct.items():
    if v > max_2_dct: max_2_dct = v

## ПОИСК второго по величине значения и его печать
for k, v in dct.items():
    if v == max_2_dct:
        print(f'II-й наибольший результат {k, v}')

