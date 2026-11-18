# Write a program that reads the names and weights of several people, storing everything in a list. At the end, display:
# A) How many people were registered.
# B) A list of the heaviest people.
# C) A list of the lightest people.

biggest = []
smallest = []
l = []
b = 0
s = 0
c = 0
while True:
    n = str(input('Name: '))
    w = float(input('Body weight: '))
    l.append(n)
    l.append(w)
    if c == 0:
        b = w
        s = w
        biggest.append(l[:])
        smallest.append(l[:])
    else:
        if w >= b:
            if w > b:
                biggest.clear()
                b = w
                biggest.append(l[:])
            elif w == b:
                biggest.append(l[:])
        if w <= s:
            if w < s:
                smallest.clear()
                s = w
                smallest.append(l[:])
            elif w == s:
                smallest.append(l[:])
    l.clear()
    c += 1
    q = str(input('Do you want to continue? [y/n]: ')).lower()
    if q != 'y' and q != 'n':
        q = str(input('Do you want to continue? [y/n]: ')).lower()
    if q == 'n':
        break
    print('=-='*20)
print('=-='*20)
print(f'{c} persons were registred')
print(f'The highest weight recorded was {b} for:', end = ' ')
for person in biggest:
    print(f'{person[0]}', end = ', ')
print('\n', '=-='*20)
print(f'The smallest weight recorded was {s} for:', end = ' ')
for person in smallest:
    print(f'{person[0]}', end = ', ')
