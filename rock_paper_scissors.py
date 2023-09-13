# We will write a rock paper scissors game in class - Complete it in this file
import random

# player_choice = "rock"
# computer_choice = "paper"

# Create a function that gets the choices, start small and test it to see how it works with set variable
def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice} # choices is only in the function

    return choices

# function to check for a win
def check_win(player, computer):
    print(f"you chose {player}, computer chose {computer}") # f is just denoting the use of variables in the string
    if player == computer:
        return "It's a tie"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors, you win"
        else:
            return "Paper covers rock, you lose"

choices = get_choices()
print(choices)
result = check_win(choices["player"], choices["computer"])
print(result)