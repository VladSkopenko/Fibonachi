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


if __name__ == '__main__':
    print(fi(10))
