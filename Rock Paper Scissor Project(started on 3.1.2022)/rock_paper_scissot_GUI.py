#PIL pip pillow has to be installed to handle the images
from tkinter import *
import random  # each module is like a class
from PIL import Image, ImageTk

# creating istance or object for class
root = Tk()

root.title = "Rock Paper Scissor Game"

# geometry for the display screen
root.geometry("1400x500")

# random module will ascept int values so we are making a dictionary with key,value pair for computer since one player is computer
computer_values = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor",
}


# To Update Messages Like 'You Loose' , 'You Win'
def msg_update(message):
    messg_label["text"] = message


# To Update Score of Computer
def comp_score_update():
    final = int(comp_score["text"])
    final += 1
    comp_score["text"] = str(final)


# To Update Score of Player
def player_score_update():
    final = int(player_score["text"])
    final += 1
    player_score["text"] = str(final)


# Win/Loose Condition Function
def win_or_loose(player, computer):

    if player == computer:
        msg_update("It's A Tie!!")
        messg_label.configure(foreground="#033E3E") #yellow

    elif player == "rock":
        if computer == "paper":
            msg_update("Computer Wins!!")
            messg_label.configure(foreground="#800000") #red
            comp_score_update()
        elif computer == "scissor":
            msg_update("You Win!!")
            messg_label.configure(foreground="#006400") #green
            player_score_update()
        else:
            msg_update("It's A Tie!!")
            messg_label.configure(foreground="#033E3E") #yellow

    elif player == "scissor":
        if computer == "rock":
            msg_update("Computer Wins!!")
            messg_label.configure(foreground="#800000") #red
            comp_score_update()
        elif computer == "paper":
            msg_update("You Win!!")
            messg_label.configure(foreground="#006400") #green
            player_score_update()
        else:
            msg_update("It's A Tie")
            messg_label.configure(foreground="#033E3E") #yellow

    elif player == "paper":
        if computer == "rock":
            msg_update("You Win!!")
            messg_label.configure(foreground="#006400")  #green
            player_score_update()
        elif computer == "scissor":
            msg_update("Computer Wins!!")
            messg_label.configure(foreground="#800000") #red
            comp_score_update()
        else:
            msg_update("It's A Tie!!'")
            messg_label.configure(foreground="#033E3E") #yellow

    else:
        pass


to_select = ["rock", "paper", "scissor"]

# Function To Choose Computer A Random From computer_values
def choice_update(choose):
    choice_computer = to_select[(random.randint(0, 2))]

    # Computer Hand Images According to the random choice
    if choice_computer == "rock":
        img_comp.configure(image=imgRockLeft)

    elif choice_computer == "paper":
        img_comp.configure(image=imgPaperLeft)

    else:
        img_comp.configure(image=imgScissorLeft)

    # Player Hand Images According to click on button by player
    if choose == "rock":
        img_player.configure(image=imgRockRight)

    elif choose == "paper":
        img_player.configure(image=imgPaperRight)

    else:
        img_player.configure(image=imgScissorRight)

    # callig win or loose function so that it can go to that function and check the conditions given there
    win_or_loose(choose, choice_computer)


# Background Color to black
root.configure(background="#36013F")

# Paths For Images
# from PIL library ImageTk.PhotoImage(Image.open) we are using to give the directory
imgRockLeft = ImageTk.PhotoImage(Image.open("rockLeft.jpeg"))
imgRockRight = ImageTk.PhotoImage(Image.open("rockRight.jpeg"))
imgPaperLeft = ImageTk.PhotoImage(Image.open("paperLeft.png"))
imgPaperRight = ImageTk.PhotoImage(Image.open("paperRight.png"))
imgScissorLeft = ImageTk.PhotoImage(Image.open("scissorLeft.png"))
imgScissorRight = ImageTk.PhotoImage(Image.open("scissorRight.png"))


# Labels For Image, it just shows the images in the GUI
img_comp = Label(root, image=imgScissorLeft)
img_comp.grid(row=1, column=0)
img_player = Label(root, image=imgScissorRight)
img_player.grid(row=1, column=5)

# Label For Scores
comp_score = Label(root, text=0, font=("arial", 60, "bold"), foreground="#7F462C")
comp_score.grid(row=1, column=2)
player_score = Label(root, text=0, font=("arial", 60, "bold"), foreground="#7F462C")
player_score.grid(row=1, column=4)

# Labels to indicate '
comp_label = Label(
    root,
    text="COMPUTER",
    font=("arial", 40, "bold"),
    background="#C5908E",
    foreground="#3F000F",
)
comp_label.grid(row=0, column=2)
player_label = Label(
    root,
    text="PLAYER",
    font=("arial", 40, "bold"),
    background="#C5908E",
    foreground="#3F000F",
)
player_label.grid(row=0, column=4)

# Label For Message
messg_label = Label(root, text="", font=("arial", 30, "bold"), background="#CD853F")
messg_label.grid(row=3, column=3)


# Checking For Button Rock
button_rock = Button(
    root,
    width=18,
    height=3,
    text="ROCK",
    background="#C48793",
    foreground="white",
    font=("arial", 20, "bold"),
    command = lambda:choice_update("rock"),
)
button_rock.grid(row=2, column=2)


# Checking For Button Paper
button_paper = Button(
    root,
    width=16,
    height=3,
    text="PAPER",
    font=("arial", 20, "bold"),
    background="#C48793",
    foreground="white",
    command = lambda:choice_update("paper"),
)
button_paper.grid(row=2, column=3)


# Checking For Button Scissor
button_scissor = Button(
    root,
    width=16,
    height=3,
    text="SCISSOR",
    font=("arial", 20, "bold"),
    background="#C48793",
    foreground="white",
    command = lambda:choice_update("scissor"),
)
button_scissor.grid(row=2, column=4)


root.mainloop()
