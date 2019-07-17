import math

radius = float(input('Enter cylinder radius : '))
depth = float(input('Enter cylinder depth : '))
area = math.pi * (radius**2)
volume = area * depth
print(round(volume, 3))
