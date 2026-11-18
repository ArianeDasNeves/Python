#Write a program that reads several integers from the keyboard. At the end of the program, display the average of all the values, as well as the largest and smallest values entered. The program should ask the user whether or not they want to continue entering values.
a = 0
b = 0
s = 0
c = ''
d = 1
while not c == 'N':
    n = int(input('Enter a number: '))
    s += n
    c = str(input('Do you want to continue? [Y/N]: ')).upper()
    if d == 1:
        a = n
        b = n
    else:
        if n > a:
            a = n
        elif n < b:
            b = n
    d += 1
print('The average is: {:.2f}'.format(s/(d-1)))
print('The greatest number is: {}'.format(a))
print('The smallest number is: {}'.format(b))