def fibonacci_list(n):
    """
    Ось це те рішення на якому я осоромився :)
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


def fibonacci_generator_list(n):
    a, b = 0, 1
    fib_sequence = []
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence



def fibonacci_up_to_limit(limit):
    fib_sequence = []
    a, b = 0, 1
    while a <= limit:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence


if __name__ == '__main__':
    print(fibonacci_list(10))
    print(fibonacci_generator_list(10))
    print(fibonacci_up_to_limit(10))