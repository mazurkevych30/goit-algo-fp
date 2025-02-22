import turtle
import math

def draw_pythagoras_tree(t, length, angle, level):
    if level == 0:
        t.forward(length)
        t.backward(length)
        return

    t.forward(length)

    t.left(angle)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, angle, level - 1)

    t.right(2 * angle)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, angle, level - 1)

    t.left(angle)
    t.backward(length)

def main():
    level = int(input("Введіть рівень рекурсії: "))

    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Pythagoras Tree Fractal")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)


    t.penup()
    t.goto(0, -250)
    t.pendown()

    draw_pythagoras_tree(t, 200, 40, level)

    turtle.done()

if __name__ == "__main__":
    main()
