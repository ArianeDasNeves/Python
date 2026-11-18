#Write a program that plays "even or odd" against the computer. The game will only end when the player loses, and it should display the total number of consecutive wins the player achieved at the end of the game.
import random
nc = random.randint(1,10)
cc = ''
d = 0
while True:
    print('-='*20)
    c = str(input('DO you choose even or odd? [E/O]: ')).upper().strip()
    while c != 'E' and c != 'O':
        c = str(input('DO you choose even or odd? [E/O]: ')).upper().strip()
    n = int(input('Enter a number from 1 to 10: '))
    if c == 'E':
        cc = 'O'
        print(f'The number of the computer is: {nc}')
        if (nc + n) % 2 == 0:
            print('You WIN!')
            d += 1
        else:
            print('You LOSE!')
            break
    if c == 'O':
        cc = 'E'
        print(f'The number of the computer is: {nc}')
        if (nc + n) % 2 == 0:
            print('You LOSE!')
            break
        else:
            print('You WIN!')
            d += 1
print(f'You win {d} times!')