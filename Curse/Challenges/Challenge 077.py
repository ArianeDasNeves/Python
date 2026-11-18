#Write a program that reads 5 numeric values and stores them in a list. At the end, display the largest and smallest values entered and their respective positions in the list.
l = []
ma = []
mb = []
for c in range(0,5):
    n = int(input('Enter a number: '))
    l.append(n)
    if n == max(l):
        ma.append(c)
    elif n == min(l):
        mb.append(c)
print(f'The highest number is {max(l)}, in the {ma} position.\nThe lowest number is {min(l)}, in the {mb} position.')