"""
Program Title: Clever Stories
Author: Mitch Diamond

Description: Mad libs-esque program that has an added part 
    that as an "a/an" check on the last sentence.

"""

adjective = input("Please enter an adjective: ")
animal = input("Please enter an animal: ")
verb1 = input("Please enter a verb: ")
exclamation = input("Please enter an exclamation: ").capitalize()
verb2 = input("Please enter another verb: ")
verb3 = input("Please enter another verb: ")
noun = input("Please enter a noun: ")

#adding an array of vowels to check for the noun starting with an vowel.
vowels = {'a', 'e', 'i', 'o', 'u'}  
properArticle = 'a'
for c in vowels:
    if noun:
        #If the noun starts with a vowel, switch the article to "an."
        if c == noun[0]:
            properArticle = 'an'  


print()
print('-------------------------------')
print('The other day, I was really in trouble. It all started when I saw a very')
print(f'{adjective} {animal} {verb1} down the hallway. "{exclamation}"! I yelled. But all')
print(f'I could think to do was to {verb2} over and over. Miraculously,')
print(f'that caused it to stop, but not before it tried to {verb3}')
print(f'right in front of my family. But not before it gave us {properArticle} {noun}.')
 


