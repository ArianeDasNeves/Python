#Create a program that reads the names and two grades for several students and stores everything in a compound list. At the end, display a report card showing each student's average, and allow the user to view each student's grades individually.

l = []
c = 0
while True:
    l.append([])
    a = str(input(f'{[c]} Name: ')).capitalize()
    s1 = float(input(f'{[c]} Score 1: '))
    s2 = float(input(f'{[c]} Score 2: '))
    m = (s1 + s2)/2
    l[c].append(a)
    l[c].append(s1)
    l[c].append(s2)
    l[c].append(m)
    c += 1
    q = str(input('Do you want to continue? [Y/N]: ')).upper()
    if q == 'N':
        break
    if q != 'Y' and q != 'N':
        q = str(input('Do you want to continue? [Y/N]: ')).upper()
    print('-' * 30)
print('-='*30)
print(f'{'STUDENT':<8} {'NAME':<8}{'AVERAGE':<8}')
for i in range(0, c):
    print(f'[{i:^6}] {l[i][0]:<8}[{l[i][3]:^6}]')
print('-='*30)
while True:
    i = int(input('Show the grade of the student?: '))
    print(f'Score 1: {l[i][1]}\nScore 2: {l[i][2]}')
    q = str(input('Do you want to continue? [Y/N]: ')).upper()
    if q == 'N':
        break
    if q != 'Y' and q != 'N':
        q = str(input('Do you want to continue? [Y/N]: ')).upper()