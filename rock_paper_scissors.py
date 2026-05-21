# Rock Paper Scissors Game

import random

# ASCII structures
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
---'    ____)____
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

# Store in list
game_images = [rock, paper, scissors]

# Game loop
while True:

    print("\n===== Rock Paper Scissors =====")
    print("0 - Rock")
    print("1 - Paper")
    print("2 - Scissors")
    print("3 - Exit")

    user_choice = int(input("Enter your choice: "))

    # Exit option
    if user_choice == 3:
        print("Game Closed!")
        break

    # Input validation
    if user_choice < 0 or user_choice > 2:
        print("Invalid choice! Try again.")
        continue

    print("\nYou chose:")
    print(game_images[user_choice])

    # Computer choice
    computer_choice = random.randint(0, 2)

    print("Computer chose:")
    print(game_images[computer_choice])

    # Conditions to determine winner
    if user_choice == computer_choice:
        print("It's a Draw!")

    elif (
        (user_choice == 0 and computer_choice == 2) or
        (user_choice == 1 and computer_choice == 0) or
        (user_choice == 2 and computer_choice == 1)
    ):
        print("You Win!")

    else:
        print("You Lose!")