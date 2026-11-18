# Write a program that reads two integers and compares them, displaying one of the following messages on the screen:
#
# – The first value is greater
#
# – The second value is greater
#
# – Neither value is greater; they are equal
a = int(input('Enter a integer number: '))
b = int(input('Enter a another integer number: '))
if a>b:
    print('The first number is greater than the second number')
elif a<b:
    print('The second number is greater than the first number')
elif a==b:
    print('The numbers are equal')
