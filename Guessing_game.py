import random

def guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize the guess count
    guess_count = 0
    
    print("\n\t\t\tWelcome to the Guessing Game! Can you guess the number between 1 and 100?\n")
    
    while True:
        # Get user input for the guess
        try:
            user_guess = int(input("\t~Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        # Increment the guess count
        guess_count += 1
        
        # Check if the guess is correct
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the correct number in {guess_count} attempts.")
            break
        elif user_guess < secret_number:
            print("\tToo low! Try again.\n")
        else:
            print("\tToo high! Try again.\n")

# Run the guessing game
guessing_game()