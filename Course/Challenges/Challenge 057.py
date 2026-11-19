#Improve the CHALLENGE 27 game, in which the computer “thinks” of a number between 0 and 10. But now the player will try to guess until they get it right, and at the end, the game will show how many guesses it took to win.
import random
from time import sleep
c = random.randint(0, 10)
n = -1
d = 0
while n != c:
    n = int(input('Enter a number from 0 to 10: '))
    d += 1
sleep(0.5)
print('=-'*20)
sleep(0.5)
print('The computer thought of the number {}'.format(c))
sleep(0.5)
print('=-'*20)
sleep(0.5)
print('You got it! You guessed in {} tries'.format(d))
sleep(0.5)
print('=-'*20)