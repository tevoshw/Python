"""
Description exercise 1: Write a program that receives a number from the user and tells whether it is odd or even

"""


# Code for this question
user_input = int(input("Enter you number here: "))
if user_input % 2 == 0:
    print(f"the number {user_input}, it's a EVEN NUMBER!")
else:
    print(f"the number {user_input}, it's a ODD NUMBER!")



# We can simplify that with this code
user_input2 = int(input("Enter your number here: "))
print(f"The number {user_input2} is a EVEN NUMBER!" if user_input2 % 2 == 0 else f"The number {user_input2} is a ODD NUMBER!")