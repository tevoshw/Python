"""

Description exercise 10:  Create a program that reads a string and counts how many words it has.

"""

# Code for this question
user_input = input("Enter the phrase string here: ")
words = user_input.split()
print(f"The phrase '{user_input}' has {len(words)} words!")