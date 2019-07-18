import turtle
import random

draw = turtle.Turtle()
lines = random.randint(10)

for i in range(lines):
    length = random.randint(10, 100)
    angle = random.randint(1, 365)
    draw.forward(length)
    draw.right(angle)
