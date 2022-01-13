# GUI of Number Guessing Game BASIC version
#only one chance


from tkinter import *
import random

# To create main window
root = Tk()
root.title("Number Guessing Game")
root.geometry("400x400")

class NumberGuessingGameGUI:

    # Variables that stores Entry values
    num1 = IntVar()
    num2 = IntVar()
    guessnum = IntVar()

    # It stores the random generated Number
    guessValue = None

    # Function for checking and generating random numbers
    def game(self):

        # It generates a random number and stores it in guessValue variable
        self.guessValue = random.randint(self.num1.get(), self.num2.get())

        # Condition that checks random number matches guessed number or not
        if self.guessValue == self.guessnum.get():

            # If matches result label text changed to given text
            self.label4.configure(text="Congratulations!, You Won The Game")
        else:

            #If not matches result label text changed to given text and random number
            self.label4.configure(text="Oops!, You Lost The Game, The Value Was : " + str(self.guessValue))

    # When the class is called this functions runs first
    def __init__(self):

        # Fonts for Label & Entry Boxes
        self.font = ("arial", 15)

        # Label 1st range
        self.label1 = Label(root, font=self.font, text="1st Range: ")
        self.label1.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        # Grid helps the Label or any Field to align in a perfect place
        # Such as in row or column

        # Entry Box For Storing 1st range Value
        self.entry1 = Entry(root, textvariable=self.num1)
        self.entry1.grid(row=0, column=1, padx=5, pady=5)

        # Label 2nd range
        self.label2 = Label(root, font=self.font, text="2nd range:")
        self.label2.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        # Entry Box For Storing 2st range Value
        self.entry2 = Entry(root, textvariable=self.num2)
        self.entry2.grid(row=1, column=1, padx=5, pady=5)

        # Label Guess Any Number
        self.label3 = Label(root, font=self.font, text="Guess The Number")
        self.label3.grid(row=3, columnspan=2, pady=5)

        # Entry Box For Number Guessing
        self.entry3 = Entry(root, textvariable=self.guessnum, font=self.font)
        self.entry3.grid(row=4, columnspan=2, pady=10, padx=5)

        # Button to check that value matches to random number or not
        self.btn = Button(root, font=self.font, text="Check", command=self.game)
        self.btn.grid(row=5, columnspan=3, pady=10)

        # Result label
        self.label4 = Label(root, font=self.font, text="")
        self.label4.grid(row=6, columnspan=3, padx=10, pady=5)

        # This opens GUI
        root.mainloop()

# Calling the class
NumberGuessingGameGUI()

# Removed root from grid() and removed bg = '' and spell of coloumnspan
# Added .get() to get none class variables
