#Write a program that reads the first term and the common ratio of an arithmetic progression. At the end, display the first 10 terms of that progression.
a1 = int(input('The first term of the arithmetic progression is: '))
r = int(input('The common ratio of the arithmetic progression is: '))
for c in range(1, 11):
    print('{}'.format(a1), end=' ')
    a1 += r