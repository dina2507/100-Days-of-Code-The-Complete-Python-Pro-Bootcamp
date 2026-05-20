import random

# Global Constants (Names written in ALL_CAPS for values that never change)
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    """Asks user for difficulty and returns the corresponding number of turns."""
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choice == "hard":
        return HARD_LEVEL_TURNS
    else:
        # Default to easy if they type anything else or 'easy'
        return EASY_LEVEL_TURNS


def check_answer(user_guess, comp_number):
    """Compares the guess with the answer and prints the hint."""
    if user_guess > comp_number:
        print("Too High.\nGuess again.")
        return False
    elif user_guess < comp_number:
        print("Too Low.\nGuess again.")
        return False
    else:
        print(f"You got it! The answer was {comp_number}.")
        return True


def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    comp_guess = random.randint(1, 100)
    attempts = set_difficulty()  # Dynamic assignment based on function return value

    # Track game state with a boolean flag
    game_over = False

    while attempts > 0 and not game_over:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))

        # Check the answer using our helper function
        game_over = check_answer(user_guess, comp_guess)

        # If they didn't guess right, penalize them an attempt
        if not game_over:
            attempts -= 1

    if attempts == 0 and not game_over:
        print("You've run out of guesses, you lose.")


# Start the game
play_game()