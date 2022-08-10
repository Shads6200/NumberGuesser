#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
import art
easy_level = 5
hard_level = 10

def check_answer(guess, answer, attempts):
  if guess < answer:
    print("Too low")
    return attempts - 1
  elif guess > answer:
    print("Too high")
    return attempts - 1
  else:
    print("Correct. You win")

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return easy_level
  elif level == "hard":
    return hard_level 


def the_game():
  print(art.logo)
  print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")
  answer = random.randint(1,100)
  attempts = set_difficulty()
  guess = 0
  while guess != answer:
    print (f"You have {attempts} attempts remaining to guess the number ")
    guess = int(input("Make a guess: "))
    attempts = check_answer(guess,answer,attempts)
    if attempts == 0:
      print("You have run out of guesses. You lose")
      return 
    elif guess != answer:
      print("Guess again")

the_game()
  
  
  