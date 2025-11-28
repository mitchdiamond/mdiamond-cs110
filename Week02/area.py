"""
Title: Area of Shapes
Author: Mitch Diamond

Description: This program will take inputs from the user and provide the area of 
shapes. Including a square, a rectangle, and a circle.


"""
#import any libraries.
import math

#get inputs from the user
squareSide = float(input("What is the length of the side of your square in centimeters? "))

rectLength = float(input("What is the length of your rectangle in centimeters? "))
rectWidth = float(input("What is the width of your rectangle in centimeters? "))

radius = float(input("What is the radius of your circle in centimeters? "))

#use inputs to get the area
#square - side squared
areaSquare = squareSide ** 2

areaRect = rectLength * rectWidth

areaCircle = math.pi * (radius ** 2)

print(f"the area of your square is {areaSquare} cm^2")
print(f"the area of your rectangle is {areaRect} cm^2")
print(f"the area of your circle is {areaCircle:.2f} cm^2")

#Enhancement: The answer in meters
print()
print(f"the area of your square is {areaSquare/10000} m^2")
print(f"the area of your rectangle is {areaRect/10000} m^2")
print(f"the area of your circle is {areaCircle/10000:.2f} m^2")


