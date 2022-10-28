import random
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
game_images = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor\n"))
if choice >= 2 or choice < 0:
    print("You print an invalid number, You lose!")
else:
    print(game_images[choice])

    comp_choice = random.randint(0, 2)
    print(game_images[comp_choice])

    if choice == 0 and comp_choice == 2:
        print("You win!")
    elif choice == 2 and comp_choice == 0:
        print("You lose!")
    elif comp_choice > choice:
        print("You lose!")
    elif choice > comp_choice:
        print("You Win!")
    elif choice == comp_choice:
        print("It's a draw.")


