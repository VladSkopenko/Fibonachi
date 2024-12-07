# Моє особисте  рішення після того як я розібрався
def fi(n):
    result = []
    if n == 0:
        return []
    if n == 1:
        return [0]
    x = 0
    y = 1
    result.append(x)
    for i in range(n):
        x, y = y, x + y
        result.append(x)
    return result


def fi_recursive(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    previous = fi_recursive(n - 1)
    next_value = previous[-1] + previous[-2]
    return previous + [next_value]


if __name__ == "__main__":
    print(fi(10))
    print(fi_recursive(10))
