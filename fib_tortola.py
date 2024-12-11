import turtle


def draw_fibonacci_spiral(n):
    a, b = 0, 1
    turtle.speed(0)

    for _ in range(n):
        turtle.forward(b * 10)
        turtle.right(90)
        a, b = b, a + b


turtle.title("Fibonacci Spiral")
turtle.bgcolor("black")
turtle.pencolor("white")


draw_fibonacci_spiral(10)


turtle.done()
