"""
Name: Mitch Diamond
Program: Passwords
Description: Password strength checker. I added a user toggle that could allow them to turn on case sensitivity.
I understand in real life it might not ncessarily be adviseable, but just to add something else in on the creativity side.
Also needed to adjust some of the parameters to carry it to the proper function.
"""

LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]

"""
This function reads a file (specified by the filename parameter) in which each line of the 
file contains a single word. If the word passed in the word parameter matches a word in the 
file the function returns a true otherwise it returns a false. If the parameter case_sensitive 
is true a case sensitive match is performed. If case_sensitive is false a case insensitive match 
is performed. The case_sensitive parameter should default to False
"""
def word_in_file(password, filename, case_sensitive = False):

    #Ensures that user can't have a password that's all caps get through.
    #Also allows for the user to change if they want to strictly follow cases.
    if case_sensitive is False:
        password = password.lower()

    with open(filename, "r", encoding="UTF-8") as word_file:
        for line in word_file:
            line = line.strip()
            if line == password:
                return True
    
    return False
    
"""
This function loops through each character in the string passed in the word parameter to 
see if that character is in the list of characters passed in the character_list parameter. 
If any of the characters in the word are present in the character list return a true, If 
none of the characters in the word are in the character list return false
"""
def word_has_character(word, character_list):
    for c in word:
        if c in character_list:
            return True
    
    return False

"""
This function creates a numeric complexity value based on the types of characters the 
word parameter contains. One point of complexity is given for each type of character in 
the word. The function calls the word_has_character function for each of the 4 kinds of 
characters (LOWER, UPPER, DIGITS, SPECIAL). If the word has that kind of character a 
point is added to complexity rating. Since there are 4 kinds of characters the complexity 
rating will range from 0 to 4. (0 would be returned only if word contained no characters 
or only contains characters that are not in any of the lists.)
"""
def word_complexity(word):
    #Complexity is one from the password length to start.
    complexity = 1
    #Each character found adds another point.
    if word_has_character(word, LOWER) is True:
        complexity += 1
    if word_has_character(word, UPPER) is True:
        complexity += 1
    if word_has_character(word, DIGITS) is True:
        complexity += 1
    if word_has_character(word, SPECIAL) is True:
        complexity += 1
    
    return complexity


"""
This function checks length requirements, checks dictionary and known-passwords, calls 
word_complexity to calculate the word's complexity then determines the password's strength 
based on the user requirements. It should print the messages defined in the requirements 
and return the password's strength as a number from 0 to 5. The min_length parameter should 
have a default value of 10. The strong_length parameter should have a default value of 16
"""
def password_strength(password, isCaseSensitive, min_length = 10, strong_legnth = 16):

  
    #Checks for bad passwords.
    topPasswordPath = 'C:\\Users\\themo\\Pathways\\CSE 110 - Intro to Programming\\110-05-Functions\\Week02\\passwords\\toppasswords.txt'
    wordList = 'C:\\Users\\themo\\Pathways\\CSE 110 - Intro to Programming\\110-05-Functions\\Week02\\passwords\\wordlist.txt'
    isTopPass = word_in_file(password, topPasswordPath, isCaseSensitive)
    if isTopPass == True:
        print("Password is a commonly used password and is not secure.")
        return 0 
    isDictionaryWord = word_in_file(password, wordList, isCaseSensitive)
    if isDictionaryWord == True:
        print("Password is a dictionary word and is not secure.")
        return 0

    #Checks for long enough password that gives a five.
    if len(password) >= 16:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    #Checks for the short password.
    elif len(password) < 10:
        print("Password is too short and is not secure.")
        return 1

    #Checks for complexity values.
    passwordComplexity = word_complexity(password)

    #Returns the number for password complexity.
    return passwordComplexity
"""
Provides the user input loop. The loop asks the user for a password to test. If that password 
is anything but "q" or "Q" call the password_strength function and report the results to the 
user. If the user enters "q" or "Q", quit the program.
"""
def main():

    caseSensitive =  input("Would you like to use case sensitivity with dictionaries (y/n)? ")
    isCaseSensitive = False
    if caseSensitive.lower() == "y":
        isCaseSensitive = True


    password = ""
    testPassword = True
    while testPassword == True:
        password = input("Please enter the password you want to check: ")

        #Quit program if q is entered.
        if password.lower() == 'q':
            testPassword = False
            break
        passwordComplexity = password_strength(password, isCaseSensitive)

        #Print complexity out here rather than needing to having to do it in several places.
        print(f"Password has a strength of {passwordComplexity}")






if __name__ == "__main__":
    main()