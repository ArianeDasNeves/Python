#Write a program that calculates the sum of all numbers that are multiples of three and fall within the range from 1 to 500.
n = 0
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        count += 1
        n += c
print('\nThe sum of all {} numbers is: {}'.format(count, n))
