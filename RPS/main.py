import random

def get_choices():
    player_choice = input("Enter Choice: Rock, Paper, Scissor")
    options = ["Rock", "Paper", "Scissor"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You choose {player}! The computer chose {computer}!")
    if player == computer:
        return "it's a tie"
    elif player == "Rock":
        if computer == "Paper":
            return "Papea Bag on yo head!! You Lose!"
        else:
            return "Rock Solid! You Win!"
    elif player == "Paper":
        if computer == "Scissor":
            return "Snip Snipped like a bitch!! You Lose!"
        else:
            return "You found Cpt Neptunes Crown! You Win!"
    elif player == "Scissor":
        if computer == "Rock":
            return "Skill Issue.. You Lose."
        else:
            return "Alright Windshitter. You Win."
        
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)