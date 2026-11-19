#Write a program that helps a MEGA SENA player generate entries. The program will ask how many entries are to be generated and will randomly select 6 numbers between 1 and 60 for each entry, adding them all to a single list.
import random
import time
n = int(input('How many games will be generate?: '))
l = [[]]
print('=-'*30)
print(f'{'GENERATING GAMES...':^60}')
print('=-'*30)
time.sleep(1)
for c in range(1, n+1):
        l.append([])
        l[c].append(random.sample(range(1, 60), 6))
        print(f'Game {c}: {l[c]}')
        time.sleep(1)
print('=-'*30)
print(f'{'FINISHED!':^60}')
print('=-'*30)

