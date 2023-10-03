## Task_7_1
# Напишите программу, которая рассчитывает НОК
# (наименьшее общее кратное) для списка натуральных чисел
# НОК чисел a, b и f - это наименьшее натуральное число,
# которое делится на каждое из этих чисел без остатка
#

# Способ I
lst = [12, 18, 24]

prod = 1
for i in lst:
    prod *= i

count = 0
for i in range(max(lst), prod + 1):
    if count == len(lst):
        break
    count = 0
    for j in range(0, len(lst)):
        if i % lst[j] == 0:
            count += 1
            if count == len(lst):
                print(f'НОК{lst} = {i}')
                break

##########################
# Способ II. долгим перебором
##########################


tes = set()
tes_1 = set()

lst.sort(reverse=True)
print(lst)

for i in range(max(lst), prod + 1):
    if i % lst[0] == 0:
        tes.add(i)
print(tes)
tes_1 = tes.copy()
for i in range(1, len(lst)):
    for j in tes:
        if j % lst[i] != 0:
            tes_1.remove(j)
print(min(tes_1))
