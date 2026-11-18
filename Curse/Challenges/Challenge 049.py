#Write a program that reads six integers and displays the sum of only the even ones. If the entered number is odd, ignore it.
s = 0
count = 0
for c in range(1, 7):
    n = int(input('Enter a number: '))
    if n % 2 == 0:
        s += n
        count += 1
print('The sum of the all {} even numbers is: {}'.format(count, s))