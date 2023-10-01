## Task_5_3
# Напечатайте ряд чисел Фибоначчи
# до введённого номера n.
#
n = 9
print(1, end=', ')
fib = [0, 1]
count = 0
while True:
    print(sum(fib), end='')
    a = fib[0]
    b = fib[1]
    fib[1] = sum(fib)
    fib[0] = b
    count += 1
    if count == n - 1: break
    print(', ', end='')
print('.', end='')


