import random
secret_number = random.randint(1, 100)
attempts = 0
print("Welcome to the Number Guessing Game!")   
print('chosse a number between 1 and 100')
while attempts <10:
    guess = int (input("Enter your guess: "))
    attempts += 1
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    elif attempts >= 10:
        print("Sorry, you've used all your attempts. The secret number was:", secret_number)
    else:
        print("Congratulations! You guessed the number!")
