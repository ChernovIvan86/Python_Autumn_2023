              # Task_6_1
# Написать функцию, которая переводит строку римских цифр в десятичное число.
# Римские цифры: I=1, V=5, X=10, L=50, C=100, D=500, M=1000.
# Важно!!!!: в римском числе не может стоят подряд более 3х одинаковых символов.
# Важно!!!!: в римском числе, если предидущий разряд меньше, то его небходимо вычисть из последующего.
# Пример: MMXXIII=2023; MMXXIV=2024; MCMXVII=1917; MCMLXI=1961; MM=2000; MDXXXLXII-1862.

st_2023='MMXXIII'
st_2024='MMXXIV'
st_1917='MCMXVII'
st_1961='MCMLXI'
st_2000='MM'
st_1862='MDCCCLXII'
def ex_rome_in_arab(st):            #объявляем функцию "ex_rome_in_arab" с её аргументом "st"
    lst = list(st)

    dct = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    for i in range(0, len(lst) - 1):
        if i == len(lst) - 1: break  # выход из цикла при условии, что сравнивать не с чем
        if dct[lst[i]] < dct[lst[i + 1]]:
            lst[i] = dct[lst[i + 1]] - dct[lst[i]]
            lst.pop(i + 1)
        else:
            lst[i] = dct[lst[i]]
    lst[-1] = dct[lst[-1]]
    return sum(lst)

st = st_1961                       #задаём значение аргумента "st" для функции "ex_rome_in_arab"
print(ex_rome_in_arab(st))         #применяем функцию "ex_rome_in_arab"
