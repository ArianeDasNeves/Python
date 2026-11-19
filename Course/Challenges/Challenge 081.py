#Write a program that reads several numbers and adds them to a list. Next, create two additional lists that will contain only the even and odd numbers entered, respectively. Finally, display the contents of the three lists that were generated.
l = []
e = []
o = []
while True:
    n = int(input('Enter a number: '))
    q = str(input('Do you enter a another number? (Y/N): ')).upper()
    l.append(n)
    if n % 2 == 0:
        e.append(n)
    else:
        o.append(n)
    if q == 'N':
        break
    if q != 'Y' and q != 'N':
        q = str(input('Do you enter a another number? (Y/N): ')).upper()
print(f'The list: {l}\nThe even numbers: {e}\nThe odd numbers: {o}')
