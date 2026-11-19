#Write a program that displays the multiplication table for various numbers—one at a time—for each value entered by the user. The program will terminate if the requested number is negative.
c = 0
while True:
    n = int(input('Enter a number: '))
    if n < 0:
        break
    print('-='*20)
    print('The multiplication table is: ')
    print('-'*20)
    for c in range(1, 11):
        print(f'{n:^3} x {c:^3} = {n*c:^3}')
    print('-=' * 20)
print('DONE')