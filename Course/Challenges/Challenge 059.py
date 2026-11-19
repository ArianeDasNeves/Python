#Write a program that reads any number and displays its factorial.
''' n = int(input('Enter a number: '))
d = n
f = ''
g = n
while not d == 1:
    d -= 1
    n *= d
    f += str('*') + str(d)
print('The factorial is {}{} = {}'.format(g, f, n)) '''

n = int(input('Enter a number: '))
c = n
f = 1
print('Calculating factorial {}! = '. format(c), end='')
while c > 0:
    print('{}'.format(c), end='')
    print('x' if c > 1 else '=', end='')
    f *= c
    c -= 1
print(f)