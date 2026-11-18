#Write a program that reads several numbers and adds them to a list. After that, display:
# A) How many numbers were entered.
# B) The list of values, sorted in descending order.
# C) Whether or not the value 5 was entered and is in the list.

l = []
c = 0
a = 0
while True:
    n = int(input('Enter a number: '))
    q = str(input('Do you want to continue? [Y/N]: ')).upper()
    l.append(n)
    if q == 'N':
        break
    if q != 'Y' and q != 'N':
        q = str(input('Do you want to continue? [Y/N]: '))
    c += 1
#    if n == 5:
#        a = 1
l.sort(reverse = True)
print(f'{'-='*20}\n{c} numbers are entered\n{'-='*20}\n{l}')
#if a == 1:
#    print(f'{'-='*20}\nThe number 5 is entered')
#else:
#    print(f'{'-='*20}\nThe number 5 is NOT entered')
if 5 in l:
    print(f'{'-=' * 20}\nThe number 5 is entered')
else:
    print(f'{'-=' * 20}\nThe number 5 is NOT entered')