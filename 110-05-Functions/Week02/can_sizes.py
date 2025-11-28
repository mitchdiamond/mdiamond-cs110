import math as math

def calcVolume(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

def calcArea(radius, height):
    area = 2 * math.pi * radius * (radius + height)
    return area

def performCalculations(name, radius, height):
    volume = calcVolume(radius, height)
    surfaceArea = calcArea(radius, height)
    print(f"{name} has a volume of {volume:.2f}")
    print(f"{name} has a surface area of {surfaceArea:.2f}")

    efficiency = volume / surfaceArea
    print(f"Storage efficiency is {efficiency:.2f}")
    print()


def main():
    names = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6z", "#8Z short", "#10", "#211", "#300", "#303"]
    radiuses = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    heights = [10.16, 11.91, 11.59,  11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    i = 0
    while i < len(names):
        performCalculations(names[i], radiuses[i], heights[i])
        i+=1



main()