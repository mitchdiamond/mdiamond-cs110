"""
Name: Mitch Diamond
Program: Tire Volume
Description: Program that gets tire dimensions in order to caclulate the volume of a tire.
   I modified the program by including a couple pricings for common sizes of tires. If price
   is not included, it will just skip printing/saving that information. 
"""

from datetime import datetime

import math

# Have the user enter a tire width in mm.
width = int(input("Enter the width of the tire in mm (ex 205): "))

# Have the user enter the aspect ratio.
aspectRatio = int(input("Enter the aspect ratio of the tire (ex 60): "))

# Have the user enter the diameter of the wheel in inches.
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate and display the tire's volume.
volume = (math.pi * math.pow(width, 2) * aspectRatio * ( width * aspectRatio + (2540 * diameter))/10000000000)

print(f"The approximate volume is volume is {volume:.2f} liters")

#Saving the date to a cleaner string.
current_date_and_time = datetime.now()
date_str = f"{current_date_and_time:%Y-%m-%d}"

#Modified section
#Setting variable for price to be negative by default.
tire_price = -1

if width == 205 and aspectRatio == 60 and diameter == 15:
    tire_price = 100.99
elif width == 225 and aspectRatio == 65 and diameter == 17:
    tire_price = 195.00
elif width == 265 and aspectRatio == 70 and diameter == 17:
    tire_price = 150.00
elif width == 235 and aspectRatio == 60 and diameter == 18:
    tire_price = 225.00
#This will indicate no price found and will skip printing.
else:
    tire_price = -1

#Auto open/close file within this loop.
with open("tire_volume.txt", mode="at") as volume_file:

    #Prints/saves the information cacluated and entered into a single line.
    print(f"{date_str}, {width}, {aspectRatio}, {diameter}, {volume:.2f}", file = volume_file)
    #If the price is one of the four sizes listed it will also save the pricing.
    if tire_price > 0:
        print(f"Tire price found of ${tire_price:.2f} per tire\n", file = volume_file)
if tire_price > 0:
    print(f"Tire price found of ${tire_price:.2f} per tire")
else:
    print("Tire price was not found for the sizing provided.")
