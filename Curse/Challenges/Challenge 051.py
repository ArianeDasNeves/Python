#Write a program that reads an integer and determines regardless of whether  it is a prime number.


#n = int(input('Enter a number: '))
#for c in range(1, n+1):
#    print(c)
#    if (n % c == 0)*3:
#        print('This is a prime number')
#    else:
#       print('Not a prime number')
n = int(input('Enter a number: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m{}\033[m'.format(c), end = ' ')
        tot += 1
    else:
        print('\033[31m{}\033[m'.format(c), end = ' ')
print('\nThe number {} was divisible {} times'.format(n, tot))
if tot == 2:
    print('It is a prime number')
else:
    print('It is not a prime number')