round_point_a = 0
round_point_b = 0
player_a_score_list = []
player_b_score_list = []
player_a_total = 0
player_b_total = 0

def add_score(current_point , new_points):
    return current_point + new_points
for each_round_point in range(1,4):
    print(f"Round {each_round_point}")
    round_point_a = str(input("Input Player A's Point e.g 8:"))
    round_point_b = str(input("Input Player B's Point e.g 10:"))
    player_a_score = 0
    player_b_score = 0
    player_a_score_list.append(add_score(player_a_score, int(round_point_a)))
    player_b_score_list.append(add_score(player_b_score, int(round_point_b)))
    player_a_total = sum(player_a_score_list)
    player_b_total = sum(player_b_score_list)
    print(f"Total Score:\n"
          f"Player A: {player_a_total}\n"
          f"Player B: {player_b_total}")
    if round_point_a > round_point_b:
        print("Player A wins this Round!")
    elif round_point_b > round_point_a:
        print("Player B wins this Round!")
    else:
        print("It's a Tie!")
if player_a_total > player_b_total:
        print("At the end of the 3 rounds player A goes Home with the ultimate Trophy🥇")
elif player_b_total > player_a_total:
        print("At the end of the 3 rounds player B goes Home with the ultimate Trophy🥇")
else:
        print("No ultimate winner was established")