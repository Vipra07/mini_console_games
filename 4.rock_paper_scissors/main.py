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


import random

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)
print(game_images[user_choice])
print(f"Computer chose\n{game_images[computer_choice]}")


if user_choice >=3 or user_choice <0:
    print("You typed an invalid number. Try again!")

elif user_choice == 0:

    if computer_choice == 1:
        print("You lose")
    elif computer_choice == 2:
        print("You win")
    else:
        print("It's a tie")

elif user_choice == 1:

    if computer_choice == 2:
        print("You lose")
    elif computer_choice == 0:
        print("You win")
    else:
        print("It's a tie")

elif user_choice == 2:

    if computer_choice == 0:
        print("You lose")
    elif computer_choice == 0:
        print("You win")
    else:
        print("It's a tie")
