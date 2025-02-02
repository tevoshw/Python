"""

Description: Ask the user to enter three numbers and then print the largest and smallest number among them.

"""

# Code for the question
numbers = []

for x in range(1, 4):
    user_input = int(input(f"Enter the {x} number here: "))
    numbers.append(user_input)

biggest_number = max(numbers)
minor_number = min(numbers)
print(f"The biggest number in the input is {biggest_number}, and the minor is {minor_number}")