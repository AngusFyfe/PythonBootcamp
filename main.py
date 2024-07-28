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
import random

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice == 0 or user_choice == 1 or user_choice == 2:
    print(game_images[user_choice])
else:
    print("You typed an invalid number")

computer_choice = random.randint(0,2)

print(f"Computer chose:") 
print(game_images[computer_choice])

if computer_choice == user_choice:
    print("It's a draw!")
elif (computer_choice == 1 and user_choice == 2) or (computer_choice == 0 and user_choice == 1) or (computer_choice == 2 and user_choice == 0):
    print("You win.")
else:
    print("You lose. ")