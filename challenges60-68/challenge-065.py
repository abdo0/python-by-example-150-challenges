import turtle

draw = turtle.Turtle()
draw.shape('turtle')

def drawOne():
  draw.right(90)
  draw.forward(100)
  draw.penup()
  draw.left(90)
  draw.forward(50)
  draw.left(90)
  draw.forward(100)
  draw.right(90)

def drawTwo():
  draw.pendown()
  draw.forward(70)
  draw.right(90)
  draw.forward(50)
  draw.right(90)
  draw.forward(70)
  draw.left(90)
  draw.forward(50)
  draw.left(90)
  draw.forward(70)
  draw.penup()
  draw.forward(50)
  draw.left(90)
  draw.forward(100)
  draw.right(90)

def drawThree():
  draw.pendown()
  draw.forward(70)
  draw.right(90)
  draw.forward(50)
  draw.right(90)
  draw.forward(45)
  draw.right(180)
  draw.forward(45)
  draw.right(90)
  draw.forward(50)
  draw.right(90)
  draw.forward(70)

drawOne()
drawTwo()
drawThree()
