import random

def number_guessing_game():
    print("\n\t\t\tWelcome to the Number Guessing Game!")
    print("\tI have selected a random number between 100 and 200. Try to guess it.")

    # Set the range for the random number
    lower_limit = 100
    upper_limit = 200
    secret_number = random.randint(lower_limit, upper_limit)

    # Initialize variables
    guess = None
    attempts = 0

    while guess != secret_number:
        try:
            # Get user input
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            elif guess < secret_number:
                print("Too low! Try again.\n")
            else:
                print("Too high! Try again.\n")

        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

if __name__ == "__main__":
    number_guessing_game()
