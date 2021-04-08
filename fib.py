def fib(num):
    x = 0
    y = 0
    while y <= num:
        print(y)

        if y == 0:
            y = y + 1
        else:
            y = y + x

        x = y - x


fib(2584)
