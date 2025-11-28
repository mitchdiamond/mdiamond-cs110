import random

def append_random_numbers(incomingList, quantity = 1):
    i = 0

    while i < quantity:
        r = random.uniform(0,100)
        r = round(r,1)
        incomingList.append(r)
        i+=1

def main():
    numbers = [16.2, 75.1, 52.3]
    append_random_numbers(numbers)
    append_random_numbers(numbers, 3)

    for n in numbers:
        print(n)

if __name__ == "__main__":
    main()