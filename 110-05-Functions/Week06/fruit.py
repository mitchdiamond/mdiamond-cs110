def clearList(myList):
   myList.clear()

def sortList(myList):
   myList.sort()

def popItem(myList):
   print(myList.pop())

def removeItem(myList, target = "banana"):
   myList.remove(target)

def addBefore(myList, target = "apple", addItem ="cherry"):
    i = 0
    foundIndex = -1

    while i < len(myList): 
        i += 1
        if myList[i] == target:
           foundIndex = i
           break
    if foundIndex >= 0:
       myList.insert(foundIndex, addItem)      

def append(myList, addStr = "orange"):
  myList.append(addStr)

def reverse(myList):
  myList.reverse()

def main():
  # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    reverse(fruit_list)
    print(f"reverse: {fruit_list}")
    append(fruit_list)
    print(f"append orange: {fruit_list}")
    addBefore(fruit_list)
    print(f"insert cherry: {fruit_list}")
    removeItem(fruit_list)
    print(f"remove banana: {fruit_list}")
    popItem(fruit_list)
    print(f"pop item: {fruit_list}")
    sortList(fruit_list)
    print(f"sorted list: {fruit_list}")
    clearList(fruit_list)
    print(f"sorted list: {fruit_list}")

main()