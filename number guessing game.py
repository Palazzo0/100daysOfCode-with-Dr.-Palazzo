import random
from art_for_num_guessing_game import logo

print("Welcome to Dr. palazzo's Number guessing game! ")

#choose a random number btw 1-100
chosen_num = random.randint(0,100)
# print(f"The chosen number is {chosen_num}")
level = input("I am guessing a number between 1 and 100, which is it? Type 'Easy' or 'Hard' to choose your difficulty level:\n").lower()

HARD = 5
EASY = 10

def guessing(u_guess, attempts, actual_answer):
    """TO CHECK THE ACTUAL ANSWER AND ALSO THE NUMBER OF ATTEMPTS LEFT"""
    if u_guess > actual_answer:
        print("Too high")
        return attempts - 1
    if u_guess < actual_answer:
        print("Too Low")
        return attempts - 1
    if u_guess == actual_answer:
        print(f"You guessed it right! it's {actual_answer} ")

# TO CHECK LEVEL DIFFICULTY
def chose_level():
    if level == "easy":
        return EASY
    else:
        if level == "hard":
            return HARD

def play_game():
    attempts = chose_level()
    guess = 0
    while guess != chosen_num:
        print(f"You have {attempts} attempts left")
        user_guess = int(input("Make a guess:\n"))
        attempts = guessing(user_guess, attempts, chosen_num)
        if attempts == 0:
            print("You have run out of guesses. You lose!\n"
                  f"the number is {chosen_num}")
        elif guess != chosen_num:
            print("Guess again")


play_game()