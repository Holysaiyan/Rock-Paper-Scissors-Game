import random
import os
from rockpaperscissors_images import rock,paper,scissors,logo

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
initial_game = False
end_of_game = False
player_score = 0
computer_score = 0

print(logo)

#Ask User how many games they want to play between 3 or 5

while not initial_game:
    turns = int(input("How many games do you want to play? 3 or 5? \n"))
    if turns == 3 or turns == 5:
        initial_game = True
    else:
        print(f"unfortunately {turns} was not part of the option, you will have to wait for future updates, please try again")
        
    necessary_wins = int(turns/2) + 1

while not end_of_game:
    game_images = [rock,paper,scissors]
    user_choice = int(input("What do you choose? Type '0' for Rock, '1' for paper or '2' for Scissors\n"))

    if user_choice > 2 or user_choice < 0:
        print(f"{user_choice} is way out of scope, please try again")
        continue
    print(game_images[user_choice])

    computer_choice = random.randint(0,2)
    print(game_images[computer_choice])

    computer_rock = ["Draw","User wins","Computer wins"]
    computer_paper = ["Computer wins","Draw","User wins"]
    computer_scissors = ["User wins","Computer wins","Draw"]

    map_computer_choice = [computer_rock,computer_paper,computer_scissors]
    map_user_computer = map_computer_choice[computer_choice][user_choice]

    print(map_user_computer)

    # Score Board

    if map_user_computer == "User wins":
        player_score += 1

    elif map_user_computer == "Computer wins":
        computer_score += 1



    print(f"Player score: {player_score}\nComputer Score: {computer_score}")

    if player_score >= necessary_wins:
        print("Player is the winner")
    elif computer_score >= necessary_wins:
        print("Computer is the winner")

    if player_score >= necessary_wins or computer_score >= necessary_wins:
        end_of_game = True


play_again = input("Do you want to play again? (y/n): ")

if play_again == "y":
    initial_game = False
elif play_again == "n":
    end_of_game = True
