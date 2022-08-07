import random
import time

while True:
    print("What will you pick?")
    choice2 = str(input())
    list = ["rock", "paper", "scissors"]
    enemychoice = random.choice(list)
    if choice2 == "rock":
        print("You picked rock.")
        if enemychoice == "scissors":
            print("I pick Scissors! You win!")
        elif enemychoice == "paper":
            print("I pick Paper! You lose!")
        elif enemychoice == "rock":
            print("I pick Rock! Its a tie!")
    elif choice2 == "paper":
        print("You picked paper.")
        if enemychoice == "scissors":
            print("I pick Scissors! You lose!")
        if enemychoice == "paper":
            print("I pick Paper! Its a tie!")
        if enemychoice == "rock":
            print("I pick Rock! You win!")
    elif choice2 == "scissors":
        print("You picked Scissors.")
        if enemychoice == "scissors":
            print("I pick Scissors! Its a tie!")
        if enemychoice == "paper":
            print("I pick Paper! You win!")
        if enemychoice == "rock":
            print("I pick Rock! You lose!")

