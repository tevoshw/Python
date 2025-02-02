"""

Description: Make a program that displays a countdown from the user input to 1.

"""

# Code for this question
user_input = int(input("Enter the number here: "))
number = user_input
while number > 1:
    print(f"The number you choose {user_input}, and now we are on the number {number}")
    number -= 1
