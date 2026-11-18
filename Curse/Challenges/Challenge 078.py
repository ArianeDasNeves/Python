#Create a program where the user can enter several numeric values and add them to a list. If a number already exists in the list, it will not be added. At the end, all unique values entered will be displayed in ascending order.
l = []
a = 0
c = 0
while True:
    n = int(input('Enter a number:'))
    q = str(input('Do you want to continue? [Y/N]: ')).upper()
    if q != 'Y' and q != 'N':
        q = str(input('Do you want to continue? [Y/N]: ')).upper()
    if q == 'N':
        break
    if c == 0:
        a = n
    else:
        if n == a:
            l.remove(n)
            print('The number exists, enter another number.')
    c += 1
    l.append(n)
print(sorted(l))