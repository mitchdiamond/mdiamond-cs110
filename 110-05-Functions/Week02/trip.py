def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.
    Parameters
    start_miles: An odometer value in miles.
    end_miles: Another odometer value in miles.
    amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    difference = end_miles - start_miles
    mpg = difference/amount_gallons



    return mpg

def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.
    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """

    liters = 235.215 / mpg

    return liters

def main():
    # Get an odometer value in U.S. miles from the user.
    start_miles = int(input("What is the starting odometer value? "))
    # Get another odometer value in U.S. miles from the user.
    end_miles = int(input("What is the ending value of the odometer? "))
    # Get a fuel amount in U.S. gallons from the user.
    spent_fuel = float(input("What is the fuel used? "))
    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_per_gallon(start_miles, end_miles, spent_fuel)
    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)
    # Display the results for the user to see.
    print(f"{mpg:.2f} miles per gallon")
    print(f"{lp100k:.2f} liters per 100 kilometers")

main()