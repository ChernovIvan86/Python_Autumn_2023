            ### Task_11_1
# Каждый третий четверг каждого месяца билеты в Эрмитаж бесплатны.
# Напечатайте список дат в 2023 году, когда вход бесплатый.

import datetime
from calendar import monthrange
year=2023

for m in range(1, 13):
    d_max = monthrange(year, m)[1]
    con = 0
    for d in range(1, d_max+1):
        if datetime.datetime(year, m, d).weekday() == 3:
            con += 1
            if con == 3:
                print(year, m, d)
