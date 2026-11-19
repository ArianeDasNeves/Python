#Write a Python program that reads any integer and asks the user to choose the base for conversion: 1 for binary, 2 for octal, and 3 for hexadecimal.
a = int(input('Enter a number: '))
b = str(input('Select:'
      '1 to convert the number to binary'
      '2 to convert the number to octal'
      '3 to convert the number to hexadecimal: '))
if b == '1':
    a1 = a%2
    a2 = a//2
    if a2 != 0:
        a3 = a%2
        a4 = a2//2