#Number Guessing Game Objectives:
import random

def set_difficulty():
    players_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if players_difficulty == 'easy':
        return 10
    else:
        return 5

def check_guess(guess, answer):
    if guess > answer:
        print("Too high.")
        return False
    elif guess < answer:
        print("Too low.")
        return False
    else:
        print(f"You got it! The answer was {answer}.")
        return True

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)

    attempts = set_difficulty()
    print(f"You have {attempts} attempts remaining to guess the number.")

    guessed_correctly = False
    while attempts > 0 and not guessed_correctly:
        guess = int(input("Make a guess: "))
        guessed_correctly = check_guess(guess, answer)
        attempts -= 1
        if not guessed_correctly and attempts > 0:
            print(f"You have {attempts} attempts remaining.")
        elif attempts == 0:
            print("You've run out of guesses. You lose.")
            print(f"The number was {answer}.")

game()


# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
        
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


