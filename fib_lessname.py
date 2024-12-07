fibonacci = lambda n: (
    [0, 1][:n] if n <= 2 else (fib := fibonacci(n - 1)) + [fib[-1] + fib[-2]]
)

print(fibonacci(10))
