#Opens/closes the file while it is in this block.
with open("Week06\CodeAlong\hr_system.txt") as open_file:

    next(open_file)

    #Loops through the file.
    for line in open_file:
        
        #Splits the lines into the individual data sections.
        parts = line.split()

        #Stores the individual data points
        name = parts[0].strip()
        idNum = int(parts[1])
        title = parts[2].strip()
        salary = float(parts[3].strip())

        paycheck = salary/24
        bonus = 1000
        if title == "Engineer":
            paycheck += bonus

        #name (ID: id_number), job_title - $salary
        
        #Prints out the information using the requested formatting.
        print(f"{name} (ID: {idNum}), {title} - ${paycheck:.2f}")
