"""

Description: Write a program that counts how many vowels there are in a user-supplied word.

"""

# Code for this question

word = input("Digite uma palavra: ").lower()
vowels = "aeiou"
vowel_count = sum(1 for letter in word if letter in vowels)
print(f"The word '{word}' have {vowel_count} vowels")
