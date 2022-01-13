# # Number Guessing Game(basic)
# This was the basic program
# Where we have limited our conditions

# It's a module
import random  

# Generate a random number between 1 to 10
num = random.randint(1, 10) 

# Initialized a variable for guess inputs
flag = None

# It's an infinite loop
# Instead of any condition make it :: while True:
while (flag != num): 

    # Taking input from user
    flag = int(input("Enter your number between 1 to 10: "))

    # This condition is used to check if user input is correct or not
    if flag == num:
        print("Congratulation you won")
        # Here we used break because our loop is infinite
        break
    else:
        print("Oops, Try Again!!")
# Modified version of Number Guessing Game

import random

# Range is given by user
rng1=int(input("enter your first desired range"))
rng2=int(input("enter your last desired range"))

# Generating random numbers between the range given by user
randm = random.randint(rng1, rng2) 

# Initialization
count = 0 

#chances of guessing no. restricted to 5 times
while (count < 5):   

    # Counting guesses
    count += 1
    
    # Taking input of guess
    guess = int(input("Enter your guess: ")) 
    if randm == guess:
        print("congratulations! You took",count, "atempts")        
        break
    
    #giving hints to the user
    elif (randm < guess):
        print("Your guess is too high!")
        
    elif (randm > guess):
         print("Your guess is too low!")
         
    else:
      print("try again")
