#Write a program that makes the computer play Jokenpô with you.
import time
p = str.strip(input('Your options: \n ROCK \n PAPER \n SCISSORS \n What is your next move? '))
l = p.upper()
time.sleep(1)
print('Rock')
time.sleep(1)
print('Paper')
time.sleep(1)
print('Scissors')
time.sleep(1)
print('GO!')
import random
time.sleep(1)
print('-='*20)
c = random.choice(('ROCK', 'PAPER', 'SCISSORS'))
print('The computer plays: {}'.format(c))
print('-='*20)
time.sleep(1)
if c == 'ROCK' and l == 'PAPER':
    time.sleep(3)
    print('You win!')
elif c == 'PAPER' and l == 'SCISSORS':
    time.sleep(3)
    print('You win!')
elif c == 'SCISSORS' and l == 'ROCK':
    time.sleep(3)
    print('You win!')
if l == 'ROCK' and c == 'PAPER':
    time.sleep(3)
    print('The Computer wins!')
elif l == 'PAPER' and c == 'SCISSORS':
    time.sleep(3)
    print('The Computer wins!')
elif l == 'SCISSORS' and c == 'ROCK':
    time.sleep(3)
    print('The Computer wins!')
if l == c:
    print('Nobody wins!')
