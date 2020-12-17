'''

Roak paper scissors
'''
import random
choice = ['rock','paper','scissor']
print("Enter how many times do you want to play with computer.")
n = int(input())
while n!=0:
    computer = random.choice(choice)
    user = input("Enter your choice\n")
    if computer == user:
        print(f"This match is tied with computer's choice being {computer}")
    elif user=='rock':
        if computer=='paper':
            print(f"Computer have won this match with computer's choice being {computer}")


        else:
            print(f"You have won this match with computer's choice being {computer}")
    elif user == 'paper':
        if computer == 'scissor':
            print(f"Computer have won this match with computer's choice being {computer}")

        else:
            print(f"You have won this match with computer's choice being {computer}")
    elif user == 'scissor':
        if computer == 'rock':
            print(f"Computer have won this match with computer's choice being {computer}")
        else:
            print(f"You have won this match with computer's choice being {computer}")
    else:
        print(f"You have enter wrong choice so computer have won this match with choice {computer}")

    n = n-1
