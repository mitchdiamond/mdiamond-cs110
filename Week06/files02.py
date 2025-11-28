people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
youngestAge = 1000
youngestName = ""

for p in people:
    data = p.split()
    name = data[0].strip()
    age = int(data[1].strip())

    if age < youngestAge:
        youngestAge = age
        youngestName = name

print(f"Youngest person is {youngestName} at {youngestAge} years old.")