# Write a program that reads four values from the keyboard and stores them in a tuple. At the end, display:
# A) How many times the number 9 appeared.
# B) In which position the first 3 was entered.
# C) Which numbers were even.
p = []
e = []
for i in range(0,4):
    n = int(input('Enter a number: '))
    p.append(n)
    if n % 2 == 0:
        e.append(n)
print(f'The number 9 appeared {p.count(9)} times\nThe number 3 was entered in the {p.index(3) if p.count(3) != 0 else 'no one'} position\nThe even numbers are: {e}')