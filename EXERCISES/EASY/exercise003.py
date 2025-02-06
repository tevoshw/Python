"""

Description exercise 3: Write a program that reads an integer and calculates the sum of all numbers from 1 to that number.

"""


# Code for this question
user_input = int(input("Enter a number here: "))
sum_numbers = 0
while sum_numbers < user_input:
    sum_numbers += 1
    print(f"You choose the number {user_input} and we are in the number {sum_numbers}")

