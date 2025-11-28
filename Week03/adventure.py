"""
Title: Choose Your Own Adventure
Author: Mitch Diamond

Description: This is my choose your own adventure program. I used methods to make it a little easier to keep track of.
I separated out some of the chunks into methods to make it a bit more manageable to visualize as I was writing it.
Along with creating a couple of loops to prompt the user properly for the choices.
"""


#Error method to compare with the choices allowed
#Loops back while the inputted word is something else.
def errorMessageTwo(wordOne, wordTwo):
   wordOut = ""
   while wordOut != wordOne and wordOut != wordTwo:
      wordOut = input(f"Please enter either {wordOne} or {wordTwo}: ").upper()
   return wordOut
#Another method that takes three inputs instead.
def errorMessageThree(wordOne, wordTwo, wordThree):
   wordOut = ""
   while wordOut != wordOne and wordOut != wordTwo and wordOut != wordThree:
      wordOut = input(f"Please enter either {wordOne}, {wordTwo}, or {wordThree}: ").upper()
   return wordOut

hasFlashlight = False
hasKey = False
hasWhistle = False

#MAIN BRANCH 2
def cabin2(item):
    print("Arriving at the cabin with your new item you open the door and go inside.")
    if item == "FLASHLIGHT":
        print("You see a dark hallway to your right.")
        playerChoice = input("Do you use FLASHLIGHT or LEAVE? ").upper()
        
        choiceOne = "FLASHLIGHT"
        choiceTwo = "LEAVE"

        if playerChoice != choiceOne and playerChoice!= choiceTwo:
            playerChoice = errorMessageTwo(choiceOne, choiceTwo)
        if playerChoice == choiceOne:
            print("Turning on the flashlight, you slowly walk down the hallway.")
            print("Approaching the door at the end of the hall you hear some excited whispering.")
            print("On opening the door you are greated with your friends shouting")
            print("HAPPY BIRTHDAY!")
        
        else:
            print()
            print("You turn around and leave.")
            print("After arriving home you recieve a call from your friends asking")
            print("why you left and find out too late they invited you to the")
            print("cabin for your birthday party.")
    if item == "WHISTLE":
        print("Since there is now a strange whistle in your possession.")
        playerChoice = input("Do you use the WHISTLE or LEAVE? ").upper()
        
        choiceOne = "WHISTLE"
        choiceTwo = "LEAVE"

        if playerChoice != choiceOne and playerChoice!= choiceTwo:
            playerChoice = errorMessageTwo(choiceOne, choiceTwo)
        if playerChoice == choiceOne:
            print()
            print("In using the strange whistle in the foyer of the house,")
            print("you hear a strange rumbling coming from the attic.")
            print("For reasons you cannot comprehend you feel compelled to follow")
            print("the sounds. On climbing the stairs into the attic")
            print("the door swings closed behind you and you hear a loud click.")
            print("As you turn around you end up fainting from the terror that you see")
            print("in front of you...")
        else:
            print()
            print("Using your better judgement, you decide not to try the whistle.")
            print("After all, you did you research before arriving at the house")
            print("and it would be silly to try the same thing that seemed to cause")
            print("all those other people to go missing...")
    if item == "KEY":
        print("Since you have a key, you notice a strange door on your left.")
        playerChoice = input("Do you use the KEY or LEAVE? ").upper()

        choiceOne = "KEY"
        choiceTwo = "LEAVE"

        if playerChoice != choiceOne and playerChoice!= choiceTwo:
            playerChoice = errorMessageTwo(choiceOne, choiceTwo)
        if playerChoice == choiceOne:
            print()
            print("Using the KEY on the door you hear some groaning coming from the basement.")
            print("Compelled to descend the stairs your heart starts to pace fearing what you")
            print("will run into. The groaning seems to become more familiar as you realize it")
            print("is your friend's dog who ran away from home a couple months ago.")
            print("Though strangely the dog seems in perfect health despite it being")
            print("so long ago...")
        else:
            print()
            print("Thinking it would be foolish to keep looking for your friends dog after all")
            print("this time, you put the KEY back in your pocket and head back to the car.")
            print("on arriving home, you see a voicemail from your friend excitingly exlciming")
            print("that their dog had come back shortly after you left cell coverage.")

def searchCar():
    print()
    print("You can check the GLOVEBOX, VISOR, and CONSOLE.")
    choiceOne = "GLOVEBOX"
    choiceTwo = "VISOR"
    choiceThree = "CONSOLE"
    playerChoice = input("which do you do? ").upper()
    
    if playerChoice != choiceOne and playerChoice!= choiceTwo and playerChoice != choiceThree:
        playerChoice = errorMessageThree(choiceOne, choiceTwo, choiceThree)
    if playerChoice == choiceOne:
        print()
        print("You find a flashlight and go back to the cabin.")
        item = "FLASHLIGHT"
    if playerChoice == choiceTwo:
        print()
        print("You find a key and go back to the cabin.")
        item = "KEY"
    if playerChoice == choiceThree:
        print()
        print("You find a whistle and go back to the cabin.")
        item = "WHISTLE"
    cabin2(item)


#MAIN BRANCH 1 
def cabin1Leave():
    print()
    print("On turning to leave you feel breathing on the back of your neck.")
    playerChoice = input("Do you RUN or FACE the presence? ").upper()

    choiceOne = "RUN"
    choiceTwo = "FACE"

    if playerChoice != choiceOne and playerChoice!= choiceTwo:
        playerChoice = errorMessageTwo(choiceOne, choiceTwo)
    if playerChoice == choiceOne:
        print()
        print("As you start running you feel a wisp of wind at your back as you start gaining speed.")
        print("You somehow end up safely back at the car. Even though you no longer feel the presence,")
        print("you still have the feeling you need to go drive a little quicker than usual.")
        print()
        print("On arriving home, you can't quite shake the feeling that something still feels off...")
    else:
        print()
        print("You spin around to face whatever is next to you. In doing so, you are unable to see anything")
        print("in front of you. A strange sense of peace comes over you, not so much a relief, but more a")
        print("sense of grim acceptance that you have been forever changed...")

def cabin1Continue():
    print()
    print("As you press foward into the house. You hear the front door slam shut and lock behind you.")
    print("the door on your left opens and you feel a frigid breeze rushing up to greet you. At the same")
    print("time you realize the hallway feels slightly less opressive.")
    playerChoice = input("Do you go through the DOOR or enter the HALLWAY? ").upper()

    choiceOne = "DOOR"
    choiceTwo = "HALLWAY"

    if playerChoice != choiceOne and playerChoice!= choiceTwo:
        playerChoice = errorMessageTwo(choiceOne, choiceTwo)
    if playerChoice == choiceOne:
        print()
        print("As you enter the door and go down the stairs, the lights in the house go out.")
        print("You also didn't notice that the door swung shut behind you as you turn around")
        print("to try to feel your way out. Feeling around on the door you also realize there")
        print("is no handle on this door as you venture down the stairs for what seems like")
        print("three stories in the dark, you turn around and find the door is still three")
        print("steps above from where you were...")    
    else:
        print()
        print("As you start down the hallway, you start to feel a sense of familiarity come over you.")
        print("When you start to see an archway indicating a room as the other features are seemingly missing,")
        print("you end up arriving somehow back in the same foyer that you just left. With the locked door on your right,")
        print("but instead of a door in front of you, you see another hallway. After several cycles of")
        print("going through hallways that are too long, you slowly start to realize something.")
        print("This house is not going to let you leave...")

def cabin1():
    print()
    print("On approaching the house, to your right you see a hallway that seems unnaturally dark")
    print("for some reason you are physically unable to bring yourself to continue in that direction.")
    print("to your left there is a strange looking door that is locked. The only way forward being a door")
    print("that you notice is slightly ajar.")
    playerChoice = input("Do you CONTINUE through the door, or LEAVE? ").upper()

    choiceOne = "CONTINUE"
    choiceTwo = "LEAVE"

    if playerChoice != choiceOne and playerChoice!= choiceTwo:
        playerChoice = errorMessageTwo(choiceOne, choiceTwo).upper
    if playerChoice == choiceOne:
        cabin1Continue()
    else:
        cabin1Leave()

#Base entry point for the program.
def startAdevnture():
    print("You arrive at a dark cabin. You can SEARCH your car or APPROACH the building.")
    choiceOne = "SEARCH"
    choiceTwo = "APPROACH"
    
    playerChoice = input("Which do you do? ").upper()
    if playerChoice != choiceOne and playerChoice!= choiceTwo:
        playerChoice = errorMessageTwo(choiceOne, choiceTwo)
    if playerChoice == choiceOne:
        searchCar()
    else:
        cabin1()

#initiate the program itself. 
startAdevnture()