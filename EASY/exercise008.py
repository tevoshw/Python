"""

Description exercise 08: Create a program that displays numbers from 1 to 100 that are divisible by 3 and 5.

"""

# Code for this question
divisible = 0
numbers = []
for x in range(1, 101):
    if x % 3 == 0 and x % 5 ==0:
        divisible += 1
        numbers.append(x)
print(f"1 to 100, have {divisible} numbers, and they are:", *(numbers))