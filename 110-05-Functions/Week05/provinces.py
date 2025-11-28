
filename = "provinces.txt"

#Open the provinces.txt file for reading.
with open(filename, "rt") as provinces_file:

    provinces = []
    references = 0
    ALBERTA = "Alberta"

    for row in provinces_file:
        clean_row = row.strip()

        provinces.append(clean_row)

    provinces.pop(0)
    provinces.pop()

    for p in provinces:
        if p == "AB":
            p = ALBERTA
            references += 1
        elif p == ALBERTA:
            references += 1

    print(provinces)

    print(f"Alberta is mentioned {references} times")


#Read the contents of the file into a list where each line of text in the file is stored in a separate element in the list.
#Print the entire list.
#Remove the first element from the list.
#Remove the last element from the list.
#Replace all occurrences of "AB" in the list with "Alberta".
#Count the number of elements that are "Alberta" and print that number.