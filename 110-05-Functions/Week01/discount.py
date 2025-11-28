from datetime import datetime

DISCOUNT_RATE = 0.1
TAX_RATE = .06

subtotal = 0.0
quantity = 1


today = datetime.now()
dow = today.weekday()

while quantity != 0:
    quantity = int(input("Enter the quantity: "))
    if quantity != 0:
        price = float(input("Enter the price: "))
        subtotal += quantity * price

print(f"Total order {subtotal}")

if dow == 1 or dow == 3 :
    if subtotal > 50:
        discount = round(subtotal *DISCOUNT_RATE, 2)
        print(f"Discount {discount}")
        subtotal -= discount

    else:
        short = 50 - subtotal
        print(f"Discount is short {short}")
tax = round(subtotal * TAX_RATE, 2)
total = subtotal + tax

print(f"Tax {tax}")
print(f"Total Due {total}")
      