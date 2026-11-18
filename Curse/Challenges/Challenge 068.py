# Write a program that reads the age and gender of several people. For each person entered, the program should ask the user whether or not they want to continue. At the end, display:
# A) how many people are over 18 years old.
# B) how many men were entered.
# C) how many women are under 20 years old.
d = 0
m = 0
v = 0
while True:
    a = int(input('What is your age?: '))
    g = str(input('What is your gender? [M/F]: ')).upper().strip()
    if g != 'M' and g != 'F':
        g = str(input('What is your gender? [M/F]: ')).upper().strip()
    print('--'*20)
    q = str(input('Do you want to continue? [Y/N]: ')).upper().strip()
    if q != 'Y' and q != 'N':
        q = str(input('Do you want to continue? [Y/N]: ')).upper().strip()
    print('-=' * 20)
    if a > 0:
        d += 1
    if g == 'M':
        m += 1
    if g == 'F' and a < 20:
        v += 1
    if q == 'N':
        break
a = f'{d} people are over 18 years old \n{m} men was registered \n{v} women are under 20 years old'
if d == 1:
    a.replace('people', 'person')
elif m == 1:
    a.replace('men', 'man')
elif v == 1:
    a. replace('women', 'woman')
print(a)