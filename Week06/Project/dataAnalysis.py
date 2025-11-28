"""
Title: Data Analysis
Author: Mitch Diamond
Purpose: Go through a large data set being able to parse out information that the user is requesting. Added ability to 
enter a country of interest and provide the min, max, and average.

"""

with open("Week06\Project\life-expectancy.csv") as open_file:
    lowestExp = 10000
    lowestCountry = ""
    lowestYear = 0

    highestExp = 0
    highestCountry = ""
    highesetYear = 0

    totalExp = 0
    totalCountriesInYear  = 0
    
    userMaxExp = 0
    userMaxCountry = ""

    userMinExp = 1000
    userMinCountry = ""

    userCountryMin = 1000
    userCountryMax = 0
    userCountryAve = 0
    userCountryPoints = 0
    userCountryTotal = 0

    #Skip headers
    next(open_file)

    userYear = int(input("Enter the year of interest: "))
    userCountry = input("Enter the country of interest: ").capitalize()

    print(f"User country is {userCountry}")

    for line in open_file:
        parts = line.split(",")

        entity = parts[0]
        code = parts[1]
        year = int(parts[2])
        lifeExp = float(parts[3])
        
        #Performing user year checks.
        if year == userYear:

            #Adding for year average
            totalExp += lifeExp
            totalCountriesInYear += 1

            if lifeExp > userMaxExp :
                userMaxExp = lifeExp
                userMaxCountry = entity

            if lifeExp < userMinExp:
                userMinExp = lifeExp
                userMinCountry = entity

        #Added creativity for user country check
        if userCountry == entity:
            #Adding data points for the average
            userCountryPoints += 1
            userCountryTotal += lifeExp

            if lifeExp > userCountryMax :
                userCountryMax = lifeExp

            if lifeExp < userCountryMin:
                userCountryMin = lifeExp

        
        #DEFAULT SECTION
        if lifeExp > highestExp :
            highestExp = lifeExp
            highesetYear = year
            highestCountry = entity

        if lifeExp < lowestExp:
            lowestExp = lifeExp
            lowestYear = year
            lowestCountry = entity

    print()
    print(f"The overall max life expectancy is: {highestExp} from {highestCountry} in {highesetYear}")
    print(f"The overall min life expectancy is: {lowestExp} from {lowestCountry} in {lowestYear}")

    averageUserExp = totalExp/totalCountriesInYear
    #User based output
    print()
    print(f"For the year {userYear}:")
    print(f"The average life expectancy across all countries was {averageUserExp} ")
    print(f"The max life expectancy was in {userMaxCountry} with {userMaxExp}")
    print(f"The min life expectancy was in {userMinCountry} with {userMinExp}")

    
    averageUserExp = userCountryTotal/userCountryPoints
    #User creativity for country check.
    print()
    print(f"For the country {userCountry}:")
    print(f"The average life expectancy for {userCountry} is {averageUserExp} ")
    print(f"The max life expectancy is {userCountryMax}")
    print(f"The min life expectancy was in {userCountryMin}")