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

print("Welcome to The Rock, Paper, Scissors Game! \nBuilt By Aditya Raj Singh \n")
print("Guidelines: \n1. Rock = 0 \n2. Paper = 1 \n3. Scissors = 2 \n")
print("Rules, if you don't know and didn't have a childhood /jk \n1. Rock beats Scissors \n2. Scissors beats Paper \n3. Paper beats Rock \n4. If you both choose the same, it's a tie \n")
user_choice = input("Lets Begin! Choose your move 0, 1, or 2 : \n")
import random
computer_choice = str(random.randint(0,2))
if user_choice == "0" :
    print(f"You: {rock}")
    if computer_choice == "0" :
        print(f"Computer: {rock}")
        print("Tie!")
    elif computer_choice == "1" :
        print(f"Computer: {paper}")
        print("You Loose!")
    else :
        print(f"Computer: {scissors}")
        print("You Win!")
elif user_choice == "1" :
    print(f"You: {paper}")
    if computer_choice == "0" :
        print(f"Computer: {rock}")
        print("You Win!")
    elif computer_choice == "1" :
        print(f"Computer: {paper}")
        print("Tie!")
    else :
        print(f"Computer: {scissors}")
        print("You Loose!")
else :
    print(f"You: {scissors}")
    if computer_choice == "0" :
        print(f"Computer: {rock}")
        print("You Loose!")
    elif computer_choice == "1" :
        print(f"Computer: {paper}")
        print("You Win!")
    else :
        print(f"Computer: {scissors}")
        print("Tie!")
