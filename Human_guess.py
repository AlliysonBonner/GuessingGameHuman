# Guessing Game - Human agent
# Here I implemented a guessing game where the computer has a secret number.
# We are trying to guess that secret number. If our guess is too high we are
# told our guess is too high. If our guess is too low we are told our guess
# is too low. If the guess is correct, we are congradulated and the program
# exits.

# Author: Alliyson Bonner
# Github: https://github.com/alliysonbonner
# Linkedin: https://www.linkedin.com/in/alliyson-bonner-6404976b/
# Email: alliyson.bonner@gmail.com
# Date: December 07 2022

# import necessary libraries
import random

def guess_game(highest_number):
  """Starts the guess game where the user must guess the correct
  number to win.

  Args:
      highest_number(int): This is the highest posible number that
      can be picked.
  """
  # Choose a random number
  random_number = random.randint(1, highest_number)
  
  # Start game loop until winning condition is met.
  guess = 0
  while guess != random_number:
    # Ask user for a guess
    guess = int(input(f'Pick a number between 1 and {highest_number}: '))
    
    # Determines if user's guess is too high or not high enough and gives the user feedback.
    if guess < random_number:
      print('Sorry, not high enough')
    elif guess > random_number:
      print("Oh no, it's too high")
      
  # Congradulate user for guessing correct answer.
  print(f"You guessed {random_number} and it's right!!! How awesome is that?!")
  
if __name__ == "__main__":
  # Greet user and prompt them for the upper bound of the gueesing game.
  # Continue to ask user for upper bound until upperbound is greater than 1.
  print("Welcome to the guessing game")
  highest_number = 0
  while highest_number <= 1:
  	highest_number = int(input('What should the highest possible number be in this \
game: '))
  
  # Start game logic.
  guess_game(highest_number)