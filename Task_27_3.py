### Task_27_3
'''
Дан список с вложенными списками.
Написать программу подсчёта числа элементов, включая вложенные списки.
'''
lst = [1,2,3,[4,5,[6], 7], 8] # 10 элементов

def el(lst):
    count = len(lst)
    for i in lst:
        if type(i) is list:
            return count + el(i)
    return count

#print(type(lst) is list)
print(el(lst))
