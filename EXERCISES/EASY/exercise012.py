"""

Description exercise 12: Create a program that reads a number and calculates its factorial.
"""


# Code for this question
user_input = int(input("Enter the number here: "))
factorial = 1
for x in range(1, user_input + 1):
    factorial *= x
print(f"The factorial of {user_input} it's {factorial}")