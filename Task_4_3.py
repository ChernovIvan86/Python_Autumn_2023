### Task_4_3
## Ввод: два предложения с пробелами и знаками препинания.
## Определиь являются ли эти предложения анаграммами
## (т.е. имеют одинаковый набор букв).
##
st_1 = 'jujy hshhshs; l, s56354mkgerk; 543mgd'.lower()
st_2 = 'aUjy hshhshs; l, s56354mkgerk; 543mgd'.lower()
d_1 = dict()
d_2 = dict()
for i in range(0, len(st_1)-1):
    if st_1[i].isalpha():
        if st_1[i] in d_1.keys():
            d_1[st_1[i]] += 1
        else:
            d_1[st_1[i]] = 1


for i in range(0, len(st_2)-1):
    if st_2[i].isalpha():
        if st_2[i] in d_2.keys():
            d_2[st_2[i]] += 1
        else:
            d_2[st_2[i]] = 1


print(st_1)
print(st_2)
print(d_1)
print(d_2)
print(d_1 == d_2)