"""
Title: Meal Price Calculator
Author: Mitch Diamond

Description: Added a suggested tip amount calculation then prompt the user for a percentage they would like. Then displays the amount to leave on the 
table. Total is shown at the very end of the program after change is given back to the customer in case tip amount would be more than the amount given.

"""

# prompts
# The price of a child's meal (floating point)
kidsPrice = float(input("What is the price of a child's meal? "))

# The price of an adult's meal (floating point)
adultsPrice = float(input("What is the price of an adult's meal? "))

# The number of children (integer)
numKids = int(input("How many children are there? "))

# The number of adults (integer)
numAdults = int(input("How many adults are there? "))
print()

# Calculate Subtotal
totalKids = kidsPrice * numKids
totalAdults = adultsPrice * numAdults
subTotal = totalKids + totalAdults

# Print subtotal
print(f"Subtotal: ${subTotal:.2f}")

#CALCULATE TIP AMOUNT
tip15 = subTotal * (15/100)
tip20 = subTotal * (20/100)
print(f"Suggested tip of 15% is ${tip15:.2f} and suggested tip of 20% is ${tip20:.2f}")
print()
customPercent = int(input("Enter tip percentage: "))
tipCustom = subTotal * (customPercent/100)
print(f"It would be suggested then to leave ${tipCustom:.2f} of cash on the table.")
print()
# Prompt user for tax rate.
taxRate = float(input("What is the sales tax rate? "))

# Compute sales tax
taxAmount = subTotal * (taxRate/100)
print(f"Sales Tax: ${taxAmount:.2f}")

# Compute total
total = taxAmount + subTotal
# Display total
print(f"Total: ${total:.2f}")
print()

# Prompt for payment amount
paidChange = float(input("What is the payment amount? "))
# Compute and display change
givenChange = paidChange - total
print(f"Change: ${givenChange:.2f}")

#Calculates in the total with the custom tip amount, separate from change given so separate amount could be added.
totalWTip = total + tipCustom
print()
print(f"Total with suggested tip would be ${totalWTip:.2f}")