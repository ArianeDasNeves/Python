#Write a program that makes the computer “think” of an integer between 0 and 5 and asks the user to try to guess the number the computer chose. The program should display on the screen whether the user won or lost.
import random
import time
number = int(input('Guess the number from 1 to 5: '))
machine = random.randint(1,5)
print('Processing...')
time.sleep(2)
print('The number is: {}'.format(machine))
if number == machine:
    print('You Winn!')
else:
    print('You Lose!')
