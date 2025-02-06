"""

Description exercise 09: Create a program that reads a temperature in Celsius and converts it to Fahrenheit.

"""


# Code for this question
user_input = int(input("Emter the value in Celcius here: "))
fahrenheit = (user_input * 9/5) + 32
print(f"{user_input} Celsius in Fahrenheit is {fahrenheit}")