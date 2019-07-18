import turtle

draw = turtle.Turtle()
draw.shape('turtle')
filled_color = ['red', 'blue', 'green']

def drawSquare():
    for i in range(4):
      draw.forward(100)
      draw.right(90)

for i in filled_color:
  draw.pendown()
  draw.color(i)
  draw.begin_fill()
  drawSquare()
  draw.end_fill()
  draw.penup()
  draw.forward(150)
draw.done()
