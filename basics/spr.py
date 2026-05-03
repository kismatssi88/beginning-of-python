import random

# Choices
choices = ["rock", "paper", "scissors"]

# Computer chooses randomly
computer = random.choice(choices);

# User input
user = input("Enter rock, paper, or scissors: ").lower()

print("Computer chose:", computer)

# Game logic
if user == computer:
    print("It's a tie!")

elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")jpp;l

elif user in choices:
    print("You lose!")

else:
    print("Invalid input!")