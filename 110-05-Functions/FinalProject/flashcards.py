import tkinter as tk
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
        self.entry_widget = tk.Entry(self.master, width=30)  # width in characters
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

    def __init__(self, master):
        self.filename = "110-05-Functions\\FinalProject\\word_list.csv"
        self.KEY_INDEX = 1
        self.ENGLISH_INDEX = 0
        self.HIRAGANA_INDEX = 2

        self.num_cards = 0
        self.batch_keys = []
        
        self.lbl_cards = Label(master,text="How many cards would you like to study (1-50): ")
        self.lbl_cards.pack(pady=20)
        self.ent_cards=IntEntry(master, lower_bound=1, upper_bound=50)
        self.ent_cards.pack(pady=20)
        self.btn_start = Button(master, text="Start Studying")
        self.btn_start.pack(pady=20)

        self.answer_text = ""

        self.master = master
        self.master.title("Flashcard App")

        self.load_card_bank(self.filename)
        
        self.btn_start.config(command=self.study_session)


        self.current_card_index = 0
        self.display_front = True

        self.card_frame = tk.Frame(master, width=400, height=200, bg="lightblue", bd=2, relief="groove")
        self.card_frame.pack(pady=20)

        self.card_text = tk.Label(self.card_frame, text="", font=("Arial", 34), bg="lightblue", wraplength=350)
        self.card_text.pack(expand=True)

        self.answer_frame = tk.Label(self.card_frame, text="", font=("Arial", 34), bg="lightblue", wraplength=350)
        self.answer_frame.pack(pady=20)
        self.answer_frame.pack(expand=True)

        self.error_txt = Label(master, text="")
        self.error_txt.pack(pady=20)

    def quit_program(self):
        quit()
    
    def load_card_bank(self, filename):
        try:   
            with open(filename, mode='r', encoding='utf-8') as file:
                csvreader = csv.reader(file)
                header = next(csvreader)
                self.cards = {lines[self.KEY_INDEX]: lines for lines in csvreader}
            return
        except FileNotFoundError:
            return[]


    def load_card(self):
        if self.cards:

            if self.current_card_index is not 0:
                self.btn_submit.config(text = "Submit Entry", command=self.check_answer)
                self.answer_frame.config(bg="lightblue")

            current_card = self.cards[self.batch_keys[self.current_card_index]]
            self.answer_text = current_card[self.ENGLISH_INDEX]
            self.answer_frame.config(text="")

            self.current_card_index += 1
            self.card_text.config(text=current_card[self.KEY_INDEX])



            if self.current_card_index >= len(self.batch_keys):
                self.card_text.config(text="No cards in deck.")
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

    root = tk.Tk()
    root.option_add("*font", "Helvetica 32")
    app = FlashcardApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()