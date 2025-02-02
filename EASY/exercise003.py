"""

Description exercise 3: Write a program that reads an integer and calculates the sum of all numbers from 1 to that number.

"""


# Code for this question
user_input = int(input("Enter a number here: "))
sum_numbers = 0
numbers = 1
numbers_list = []  
while sum_numbers < user_input:
    sum_numbers += numbers
    numbers_list.append(numbers)
    numbers += 1

print(f"You choose the number {sum_numbers} and the way for this is: ({' + '.join(map(str, numbers_list))})")
