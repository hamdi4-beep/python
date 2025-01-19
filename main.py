def fib(n: int) -> None:
    a, b = 0, 1

    while a < n:
        print(f'a: {a}, b: {b}')
        a, b = b, a + b

fib(10)