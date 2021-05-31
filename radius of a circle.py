#### Write a python program which accepts the radius of a circle from the user and computes the area.

from math import pi


radius = float(input("please enter the circle radius, to compute the area:  "))
print("The area of the circle with a radius of " + str(radius) + " is: " + str(pi * radius**2))
