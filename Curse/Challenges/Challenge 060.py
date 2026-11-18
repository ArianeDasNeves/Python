#Repeat CHALLENGE 50 by reading the first term and the common ratio of an arithmetic progression and displaying the first 10 terms of the progression using a `while` loop.
a1 = int(input('The first term of the arithmetic progression is: '))
r = int(input('The ratio of the arithmetic progression is: '))
n = 0
print('The arithmetic progression is: ')
while n < 10:
    a1 += r
    n += 1
    print(a1-r, end = ' ')