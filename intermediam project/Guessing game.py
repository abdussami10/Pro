"""
Imagine creating a Python guessing game where you try to guess a number between 1 and 100. Describe the method that returns the method's feedback, such as "Too low! Try again" if the guessed number is less than the secret number or "Try too much" if the guess is too high.
"""

import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = input("Enter your guess (or 'exit' to quit): ")
        
        # Check if the user wants to exit
        if guess.lower() == 'exit':
            print("Thanks for playing. Goodbye!")
            break
        
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# Start the game
guessing_game()