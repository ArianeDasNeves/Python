#Write a program that reads any real number from the keyboard and displays its integer part on the screen.
from math import trunc
n = float(input('Enter a number: '))
print('The integer part of the number {} is {}'.format(n, trunc(n)))
