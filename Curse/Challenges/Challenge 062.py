#Write a program that reads any integer N and displays the first N elements of a Fibonacci sequence on the screen.
n = int(input('Enter a number: '))
c = 0
f1 = 0
f2 = 0
fn = 0
print('The fibonacci sequence is: ')
while c < n:
    c +=  1
    if c == 1:
        fn = 1
    elif c == 2:
        fn = 1
        f2 = fn
    elif c >= 3:
        f1 = f2
        f2 = fn
        fn = f1 + f2
    print(fn, end = ' -> ' if c < n else '')
