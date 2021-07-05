# Project 4 - Rock, Paper, Scissors

import random
print("Rock, Paper, Scissors - Game")
print("===========================================")

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

user_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors : "))
computer_choose = random.randint(0, 2)

rps = [rock, paper, scissors]
print("User choosen :")
print(rps[user_choose])
print("Computer choosen :")
print(rps[computer_choose])

if user_choose == 0 and computer_choose == 0:
    print("Draw")
elif user_choose == 0 and computer_choose == 1:
    print("You Lose !!!")
elif user_choose == 0 and computer_choose == 2:
    print("You Win !!!")

if user_choose == 1 and computer_choose == 0:
    print("You Win !!!")
elif user_choose == 1 and computer_choose == 1:
    print("Draw")
elif user_choose == 1 and computer_choose == 2:
    print("You Lose !!!")

if user_choose == 2 and computer_choose == 0:
    print("You Lose !!!")
elif user_choose == 2 and computer_choose == 1:
    print("You Win !!!")
elif user_choose == 2 and computer_choose == 2:
    print("Draw")

