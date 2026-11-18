#Write a program that reads several integers from the keyboard. The program will not stop until the user enters the value 999, which is the termination condition. At the end, display how many numbers were entered and their sum (ignoring the flag).
n = 0
s = 0
c = 0
while not n == 999:
    n = int(input('Enter a number from 1 to 998, 999 if you want to stop: '))
    c += 1
    s += n
print('You entered {} numbers and the sum of these numbers is: {}'.format(c-1, s-999))
