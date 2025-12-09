import tkinter
import csv
from tkinter import *
from number_entry import IntEntry
import random
import sys

class FlashcardApp:

    #Function that sets up the frame for the study session.
    def study_session(self):
        try:
            self.num_cards = self.ent_cards.get()
            for i in range (0, self.num_cards):
                random_key = random.choice(list(self.cards.keys()))
                self.batch_keys.append(random_key)

            print(self.batch_keys)

        except ValueError:
            self.error_txt.config(text="You must enter a valid number of cards")
            return
        
        self.load_card()
        self.lbl_cards.destroy()
        self.ent_cards.destroy()
        self.btn_start.destroy()

        self.lbl_answer = Label(self.master,text="What is the above Kanji in English? ")
        self.lbl_answer.pack (side=TOP)
        self.entry_widget = tkinter.Entry(self.master, width=30)
        self.entry_widget.pack(pady=10)

        self.btn_submit = Button(self.master, text="Submit Entry")
        self.btn_submit.pack(pady=20)
        self.btn_submit.config(command=self.check_answer)


    def check_answer(self):
        print(self.answer_text)
        self.btn_submit.config(text="Next Card", command=self.load_card)

        if self.answer_text.lower() == self.entry_widget.get():
            self.answer_frame.config(bg="green", text=f"Correct! {self.answer_text}")
        else:
            self.answer_frame.config(bg="deep pink", text=f"Incorrect, answer is: {self.answer_text}")

    #Class constructor. Takes in a tkinter frame. 
    def __init__(self, master):
        self.filename = "110-05-Functions\\FinalProject\\word_list.csv"
        self.KEY_INDEX = 1
        self.ENGLISH_INDEX = 0

        self.num_cards = 0
        #Array of keys based on how many cards the user wishes to do.
        self.batch_keys = []
        
        #Prompts the user for how long the session will be.
        self.lbl_cards = Label(master,text="How many cards would you like to study (1-50): ")
        self.lbl_cards.pack(pady=20)
        self.ent_cards=IntEntry(master, lower_bound=1, upper_bound=50)
        self.ent_cards.pack(pady=20)
        self.btn_start = Button(master, text="Start Studying")
        self.btn_start.pack(pady=20)

        #Set object variable to keep track of answer text without having to reference the object several times.
        self.answer_text = ""

        self.master = master
        self.master.title("Flashcard App")

        #Gets the general dictionary of the vocab.
        self.load_card_bank(self.filename)
        
        #Once the button is pushed it'll generate the keys.
        self.btn_start.config(command=self.study_session)


        self.current_card_index = 0

        #General outer frame of the program.
        self.card_frame = tkinter.Frame(master, width=400, height=200, bg="lightblue", bd=2, relief="groove")
        self.card_frame.pack(pady=20)

        #Prompt section
        self.card_text = tkinter.Label(self.card_frame, text="", font=("Arial", 34), bg="lightblue", wraplength=350)
        self.card_text.pack(expand=True)

        #Prompt answer
        self.answer_frame = tkinter.Label(self.card_frame, text="", font=("Arial", 34), bg="lightblue", wraplength=350)
        self.answer_frame.pack(pady=20)
        self.answer_frame.pack(expand=True)

        #Error section.
        self.error_txt = Label(master, text="")
        self.error_txt.pack(pady=20)

    #Function to be called when the quit button is pressed.
    def quit_program(self):
        quit()
    
    #Function to be called to load the vocab dictionary.
    #Takes in the filename of the CSV
    def load_card_bank(self, filename):
        #Try/except block for attempting to get the vocab.
        try:   
            with open(filename, mode='r', encoding='utf-8') as file:
                csvreader = csv.reader(file)
                header = next(csvreader)
                self.cards = {lines[self.KEY_INDEX]: lines for lines in csvreader}
            return
        except FileNotFoundError:
            print("Please check the filename path in init and ensure the file is in the same folder.")

    #Loads the next individual card.
    def load_card(self):

        #Checks that the cards item is valid
        if self.cards:

            #Checks that it isn't the first card and if it isn't, 
            #edits the button back to submit answer and resetting answer frame.
            if self.current_card_index is not 0:
                self.btn_submit.config(text = "Submit Entry", command=self.check_answer)
                self.answer_frame.config(bg="lightblue")

            #Sets the current card object.
            current_card = self.cards[self.batch_keys[self.current_card_index]]
            #Sets the answer text object to the correct English answer
            self.answer_text = current_card[self.ENGLISH_INDEX]
            self.answer_frame.config(text="")

            self.card_text.config(text=current_card[self.KEY_INDEX])
            #Advances the index
            self.current_card_index += 1



            #If the index is at the end, destroys the other frames and adds a quit button.
            if self.current_card_index >= len(self.batch_keys):
                self.card_text.config(text="No cards left in session.")
                self.lbl_answer.destroy()         
                self.entry_widget.destroy()
                self.btn_start.destroy()
                self.btn_submit.destroy()

                self.btn_quit = Button(self.master, text="Quit?")
                self.btn_quit.pack(pady=20)
                self.btn_quit.config(command=self.quit_program)
        else:
            self.card_text.config(text="No cards in deck.")


def main():

    root = tkinter.Tk()
    root.option_add("*font", "Helvetica 32")
    app = FlashcardApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()