"""

Generate a random integer from a to b. You and your friend have to guess a number between two numbers a and b. a and b
are inputs taken from the user. Your friend is player 1 and plays first. He will have to keep choosing the number and
your program must tell whether the number is greater than the actual number or less than the actual number. Log the
number of trials it took your friend to arrive at the number. You play the same game and then the person with minimum
number of trials wins! Randomly generate a number after taking a and b as input and don’t show that to the user.
"""
import random

try:
    print("enter value of a and b")
    a = int(input())
    b = int(input())
except:
    print("Wrong type of input")
    exit()

flag = 0
c=0
while flag<2:
    hidden = random.randrange(a, b)
    friend = c
    c = 0
    while True:
        c = c + 1
        if flag == 0:
            print("Ask your friend to enter")
        else:
            print("Enter yourself")
        var = int(input())
        if var > hidden:
            print("Number is greater choose smaller number")
        elif var < hidden:
            print("Number is smaller choose greater number")
        else:
            print("This is the exact number you can stop total chances used are ", c)
            break
    flag = flag+1
user = c
if friend<user:
    print("Your friend have won! :)")
elif user<friend:
    print("you have won! :)")
else:
    print("It's a tie :(")
