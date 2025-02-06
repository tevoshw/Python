"""

Description exercise 13:Create a program that takes a list of numbers, print them, and calculates the sum of them all.

"""



# Code for this question
numbers = []
user_input = int(input("Let's enter the list with some values, how many numbers do you want?: "))
for x in range(1, user_input + 1):
    user_input2 = int(input(f"Enter the value for the {x} indice of the list: "))
    numbers.append(user_input2)
print("\n")


for x, value in enumerate(numbers):
    print(f"The {x + 1} indice has the value of {value}")

print("\n")
print(f"And the sum of all the numbers of the list it's {sum(numbers)}")