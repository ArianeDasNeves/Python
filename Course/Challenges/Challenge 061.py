#Improve CHALLENGE 60 by asking the user if they want to display a few more terms. The program will exit when the user says they want to display 0 terms.
a1 = int(input('The first term of the arithmetic progression is: '))
r = int(input('The ratio of the arithmetic progression is: '))
n = 0
t = 11
print('The arithmetic progression is: ')
while n < 10:
    a1 += r
    n += 1
    print(a1-r, end = ' -> ' if n <= 9 else '')
while t > 10:
    t = int(input('\nHow many times do you want to continue?: ')) + 10
    while n < t:
        a1 += r
        n += 1
        print(a1-r, end = ' -> ' if n <= t-1 else '')
    n = 10