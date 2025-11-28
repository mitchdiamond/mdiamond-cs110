file_location = "Week06/books.txt"

with open (file_location) as file_data:
    for line in file_data:
        line = line.strip()
        print(line)