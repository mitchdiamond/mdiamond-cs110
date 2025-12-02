"""
Name: Mitch Diamond
Program: Receipt
Program that uses a products CSV to get product names and prices as well as another for an order request with the
product ids and quantity. Generates a receipt with the proper information.

Creativity goal was adding the 30 day return period.

"""

import csv
import datetime

def read_dictionary(filename, key_column_index):
    r_dictionary={}

    try: 
        with open (filename, 'rt') as csv_file:
            csvreader = csv.reader(csv_file, delimiter=",")
            next(csvreader)
            for row in csvreader:
                key_value = row[key_column_index]
                if key_value not in r_dictionary:
                    r_dictionary[key_value] = row
    except FileNotFoundError:
        print("Error: missing file")
        print("[Errno 2] No such file or directory: 'products.csv'")
    return r_dictionary





def main():
    KEY_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2
    QAUNTITY_INDEX = 1
    COMPANY_NAME = "Inkom Emporium"
    TAX_RATE = 0.06
    RETURN_PERIOD = 30

    products_dict = read_dictionary("110-05-Functions\\Week05\\project\\products.csv", KEY_INDEX)

    print(COMPANY_NAME)
    
    subtotal = 0
    totalItemCount = 0

    FILE_NAME = "110-05-Functions\\Week05\\project\\request.csv"
    with open (FILE_NAME, 'rt') as csv_file:
        csvreader = csv.reader(csv_file, delimiter=",")
        next(csvreader)
        for row in csvreader:
            key_value = row[KEY_INDEX]

            try:
                products_dict[key_value]

            except KeyError:

                print("Error: unknown product ID in the request.csv file.")
                print(row[KEY_INDEX])

            code_values = products_dict.get(key_value)
            name = code_values[NAME_INDEX]

            price = float(code_values[PRICE_INDEX])
            quant = int(row[QAUNTITY_INDEX])
            print(f"{name}: {quant} @ {price}")

            itemTotal = price * quant
            subtotal = subtotal + itemTotal
            totalItemCount = quant + totalItemCount


                

    taxAmount = subtotal * TAX_RATE
    totalAmount = subtotal + taxAmount

    print(f"Number of Items: {totalItemCount:.2f}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {taxAmount:.2f}")
    print(f"Total: {totalAmount:.2f}")

    print(f"Thank you for shopping at {COMPANY_NAME}")
    current_datetime = datetime.datetime.now()
    print(current_datetime)
    # Wed Nov  4 05:10:30 2020
    print(current_datetime.strftime("%a %b  %d %X %Y"))

    return_date = current_datetime + datetime.timedelta(days=RETURN_PERIOD)

    print("Return products by the date below.")
    print(return_date.strftime("%a %b %d %Y"))

if __name__ == "__main__":
    main()