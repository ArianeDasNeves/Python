# Write a program that reads two values and displays a menu on the screen:
# [ 1 ] add
# [ 2 ] multiply
# [ 3 ] greater than
# [ 4 ] new numbers
# [ 5 ] exit the program
# Your program should perform the requested operation in each case.
from time import sleep
n = float(input('Enter a number: '))
m = float(input('Enter a another number: '))
o = 0
sleep(0.5)
while not o == 5:
    o = int(input('Choose an option:\n[1]ADDITION\n[2]MULTIPLICATION\n[3]THE BIGGEST NUMBER\n[4]NEW NUMBERS\n[5]EXIT THE PROGRAM\nYour option: '))
    if o == 1:
        print('The addition is {}'.format(n +m))
    if o == 2:
        print('The multiplication is {}'.format(n*m))
    if o == 3:
        if n > m:
            print('The biggest number is {}'.format(n))
        else:
            print('The biggest number is {}'.format(m))
    if o == 4:
        n = float(input('Enter a number: '))
        m = float(input('Enter a another number: '))
    print('=-'*20)
    sleep(1)
print('You exited the program')
