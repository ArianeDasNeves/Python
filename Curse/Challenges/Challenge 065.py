#Write a program that reads integers from the keyboard. The program will not stop until the user enters the value 999, which is the termination condition. At the end, display how many numbers were entered and their sum (ignoring the flag).
n = c = s = 0
while True:
    n = int(input('Enter a number: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'{c} numbers were entered and their sum is: {s}')