"""

Description exercise 11: Create a program that reads a word and checks if it is a palindrome (that is, if it can be read the same way backwards).

"""


# Code for this question
user_input = input("Enter you word here: ")
if user_input == user_input[::-1]:
    print(f"The word {user_input} it's a palindrome, and your reverse it's {user_input[::-1]}")
else:
    print(f"The word {user_input} isn't a palindrome, and your reverse it's {user_input[::-1]}")
