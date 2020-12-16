'''

Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect
whether the entered input is age or year of birth and tell the user when they will turn 100 years old.

Here are a few instructions that you must have to follow:

Do not use any type of modules like DateTime or date utils. \
Users can optionally provide a year, and your program must tell their age in that particular year.
Your code should handle all sort of errors like:                       \
You are not yet born
You seem to be the oldest person alive
You can also handle any other errors, if possible!
'''

year = int(input("Enter the current year\n"))
print("Enter age or year of birth as an input")
ay = (input())
i = int(ay)
if len(ay)== 4:

    print("You will turn 100 years old in year ",100+i)
    print("Do you want to know your age in any particular year if not enter -1 otherwise enter the year")
    yy = int(input())
    if yy != -1:
        if yy < i:
            raise  Exception("You are not born yet.")
        elif(yy-i>100):
            print("you will be one of oldest person alive")

        print("Your age will be ",yy-i)

else:
    print("You will turn 100 years old in year ",100+year-i)
    print("Do you want to know your age in any particular year if not enter -1 otherwise enter the year")
    yy = int(input())
    if yy != -1:
        bornyear = year-i
        if yy < bornyear:
            raise  Exception("You are not born yet.")
        elif (yy-bornyear > 100):
            print("you will be one of oldest person alive")

        print("Your age will be ", yy-bornyear)


