import random
import RPSSettings
user_choice_indx = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."))
user_choice = RPSSettings.game_options[user_choice_indx]

computer_choice_indx = int(random.randint(0,2))
computer_choice = RPSSettings.game_options[computer_choice_indx]

print("User: ")
print(user_choice)
print("Computer: ")
print(computer_choice)

if user_choice_indx >= 3 or user_choice_indx < 0:
    print("Invalid Number")

if user_choice_indx == computer_choice_indx:
    print("Tie, try again...")
elif user_choice_indx == 0 and computer_choice_indx == 2:
    print("You Win!")
elif user_choice_indx == 0 and computer_choice_indx == 1:
    print("You Lose, try again...")
elif user_choice_indx == 1 and computer_choice_indx == 0:
    print("You Win!")
elif user_choice_indx == 1 and computer_choice_indx == 2:
    print("You Lose, try again...")
elif user_choice_indx == 2 and computer_choice_indx == 0:
    print("You Lose, try again...")
elif user_choice_indx == 2 and computer_choice_indx == 1:
    print("You Win!")
else:
    print("edge case")
