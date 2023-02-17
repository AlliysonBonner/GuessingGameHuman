import random

def guess_game(highest_number):
    """Starts a guessing game where the user must guess a random number between
    1 and the given highest number to win.

    Args:
        highest_number: An integer representing the highest possible number
            that can be picked.

    Returns:
        None. Prints messages to the console to guide the user through the game.
    """
    # Choose a random number
    random_number = random.randint(1, highest_number)

    # Start game loop until winning condition is met
    while True:
        # Ask user for a guess
        try:
            guess = int(input(f'Pick a number between 1 and {highest_number}: '))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        # Give user feedback on guess
        if guess < random_number:
            print('Sorry, too low')
        elif guess > random_number:
            print("Oh no, too high")
        else:
            # Congratulate user for guessing correct answer
            print(f"Congratulations! You guessed {random_number} and it's right!")
            break

if __name__ == "__main__":
    # Greet user and prompt them for the upper bound of the guessing game
    while True:
        try:
            highest_number = int(input('What should the highest possible number be in this game: '))
            if highest_number > 1:
                break
            else:
                print("Invalid input. Please enter an integer greater than 1.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Start game logic
    guess_game(highest_number)
