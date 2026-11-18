# Write a program that reads a person's full name and displays:
# – The name with all letters in uppercase and lowercase.
# – The total number of letters (not including spaces).
# – The number of letters in the first name.
name = input('What is your name? ')
print(name.upper())
print(name.lower())
name2 = name.split()
name3 = len(name) - len(name2) + 1
print(name3)
print(len(name2[0]))
