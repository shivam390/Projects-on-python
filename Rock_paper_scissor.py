rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇
import random

result = [rock, paper, scissors]
user_choice = int(input("Enter 0 from rock, 1 for paper and 2 for scissors.\n"))
print(result[user_choice])
com_choice = random.randint(0, 2)
print("Computer Choice:")
print(result[com_choice])
if user_choice > 3 and user_choice < 0:
    print("You have entered invalid number, You Lost!")
elif user_choice == 0 and com_choice == 2:
    print("You Won!")
elif com_choice == 0 and user_choice == 2:
    print("You Lose")
elif com_choice > user_choice:
    print("You Lose")
elif user_choice == com_choice:
    print("It's a Draw")
elif user_choice > com_choice:
    print("You Win!")
