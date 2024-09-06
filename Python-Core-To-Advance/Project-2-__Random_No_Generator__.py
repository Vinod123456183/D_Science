import random

def guess(n):
    rn = random.randint(1,10)  # Random number between 1 and 10
    guess = 0
    while guess != rn:  # Loop until the guess matches the random number
        try:
            guess = int(input("Enter your guess (between 1 and 10): "))  # Attempt to convert user input to an integer
        except ValueError:  # If input cannot be converted to an integer, handle the exception
            print("Please enter a valid number.")  # Inform the user of the invalid input
            continue  # Skip the rest of the loop and prompt the user again
        if guess > rn:
            print("High no ")  # Inform the user that the guess is too high
        elif guess < rn:
            print("low No")  # Inform the user that the guess is too low
        else:
            print("Perfect")  # Inform the user that the guess is correct
            break  # Exit the loop when the guess is correct
guess(10)
