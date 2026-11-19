#Rewrite CHALLENGE 11 to display the multiplication table for a number chosen by the user, but this time using a for loop.
n = int(input('Enter a number to show its multiplication table: '))
c = 0
print('=-'*20)
for c in range(0, 11):
    print('{:^3} * {:^3} = {:^3}'.format(n, c, n*c))
    c +=1
print('=-'*20)