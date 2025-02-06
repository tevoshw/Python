"""

Description exercise 2: Create a program that displays a table of a user-supplied number (from 1 to 10).

"""



# Code for this question
user_input = int(input("Enter you number here: "))
print(f"\nTable of {user_input}\n")
for x in range(1,11):
    table = user_input * x
    print(f"{user_input} x {x} == {table}")



# We can simplify that with this code
user_input2 = int(input("Enter a number: "))
print(f"\nTable of {user_input2}\n")
for x in range(1, 11):
    print(f"{user_input2} x {x} = {user_input2 * x}")

