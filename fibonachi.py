def fibonacci_recursive(n):
    """
    Це найропростіша  базова реалізація за допомоогою рекурсій

    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    """Так званий ітеративний підхід"""
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]


def fibonacci_generator(n):
    """
    Фібоначі генератор
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    print(fibonacci_recursive(10))
    print(fibonacci_iterative(10))
    print(list(fibonacci_generator(10)))
