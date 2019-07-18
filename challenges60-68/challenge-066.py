import turtle
import random

draw = turtle.Turtle()
draw.shape('turtle')
for i in range(8):
  draw.pencolor(random.choice(['red','black','green','yellow','blue','orange']))
  draw.forward(100)
  draw.right(45)
