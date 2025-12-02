import csv
import os

def read_dictionary(filename, key_column_index):
    s_dictionary={}

    with open(filename, 'rt') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)
        for row in csvreader:
            key_value = row[key_column_index]
            s_dictionary[key_value] = row

    return s_dictionary

def main():
    # os.chdir('../')
    KEY_INDEX = 0
    NAME_INDEX = 1
    students = read_dictionary("110-05-Functions\\Week05\\codeAlong\\students.csv", KEY_INDEX)
    print(students)

    iNumber = input("Please enter an I-Number: ")
    iNumber = iNumber.replace("-", "")
    if iNumber in students:
        student = students[iNumber]
        name = student[NAME_INDEX]
        
        print(f"The students name is {name}.")
    else:
        print("No such student.")


if __name__ == "__main__":
    main()