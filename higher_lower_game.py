import random
from higher_game_data import data
import art

def higher_lower_game():
    print(art.higher_logo)
    # TO ASSIGN RANDOM DATA TO A & B
    celeb_a = random.choice(data)
    celeb_b = random.choice(data)
    # THIS IS SO THAT THERE ARE NO CLASHES OR DUPLICATES
    while celeb_a == celeb_b:
        celeb_b = random.choice(data)

    # GIVE PLAYER THEIR SCORE AS WELL AS ASK THEM TO CHOOSE
    score = 0
    game_should_continue = True
    while game_should_continue:
        print(f"COMPARE A: {celeb_a['name']}, a {celeb_a['description']}, from {celeb_a['country']}\n")
        print(f"{art.higher_vs}\n")
        print(f"AGAINST B: {celeb_b['name']}, a {celeb_b['description']}, from {celeb_b['country']}\n")
        guess = input("Who has more Followers? A or B: \n").lower()
        celeb_a_followers = celeb_a['follower_count']
        celeb_b_followers = celeb_b['follower_count']

        # SET THE CORRECT ANSWER
        correct_answer = "a" if celeb_a_followers > celeb_b_followers else "b"
        if guess == correct_answer:
            score += 1
            print(f"You are right! Current score : {score}.")

            # TO MAKE B BECOME A IN THE NEXT ROUND
            celeb_a = celeb_b
            celeb_b = random.choice(data)
            # DO SAME THING HERE TO AVOID CLASHES
            while celeb_a == celeb_b:
                celeb_b = random.choice(data)
        else:
            print(f"You are wrong. The correct answer is {correct_answer}.\n Final Score : {score}.\n Game 0ver!")
            if input("Do you want to play again? 'y' or 'n': ").lower() == "y":
                print("\n" * 100)
                higher_lower_game()
            else:
                game_should_continue = False

higher_lower_game()