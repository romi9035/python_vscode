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
list = [ rock, paper, scissors ]
user_input = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
comp_input = random.randint(0,2)


if user_input >= 3 or user_input < 0:
    print("Invlid input")
else:
    print(list[user_input])
    print("Computer chose:\n")
    print(list[comp_input])
    if user_input == comp_input:
        print("Draw")
    elif user_input == 0 and comp_input == 2:
        print("You win!")
    elif comp_input == 0 and user_input == 2:
        print("You Lose!")
    elif comp_input > user_input:
        print("You Lose!")
    elif user_input > comp_input:
        print("You win!")

