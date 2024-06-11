# Program - Calculate the area of circle
# Input - Radius and Output - area

# Data Types
# input -> int or float -> float
# output -> float

# Formula - pi*r*r = 3.14

import math

radius = float(input("Enter the radius\n"))
print(math.pi)
area = math.pi * (radius ** 2)
area2 = math.pi * (math.pow(radius, 2))
print(area)
print(area2)
