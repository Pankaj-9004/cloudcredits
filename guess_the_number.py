import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    
    attempts = 0
    guess = None
    
    # Loop until the correct guess
    while guess != number_to_guess:
        # Take input from the user
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        # Provide feedback
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")

# Call the function to start the game
guess_the_number()
