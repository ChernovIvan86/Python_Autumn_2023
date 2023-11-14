### Task_24_1
'''
Напишите функцию, которая сортирует числовой список,
не используя ни каких функций, вроде
sort, sorted, max, min и т.д.
'''

lst = [2, 5, 3, 3, 1]
lst = [1, 2, 3, 4, 5]
def sort_lst(list):
    """
    :param list:
    :return: sorted list
    """
    count = 0
    while True:
        halyava = 0
        for i in range(0, len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i + 1], lst[i] = lst[i], lst[i + 1]
            else:
                halyava += 1
                if halyava >= 4:
                    return lst
        count += 1
        if count >= len(lst):
            return lst

print(sort_lst(lst))

