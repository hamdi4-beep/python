def fib(n: int) -> list:
    a, b = 0, 1
    results = []

    while a < n:
        results.append(a)
        a, b = b, a + b

    return results