#Write a program that reads any integer and displays its multiplication table on the screen.
n = int(input('Enter a number to show its multiplication table: '))
n1 = n*1
n2 = n*2
n3 = n*3
n4 = n*4
n5 = n*5
n6 = n*6
n7 = n*7
n8 = n*8
n9 = n*9
n10 = n*10
print('The Multiplication table is \n {:^3}x  1 ={:^5} \n {:^3}x  2 ={:^5} \n {:^3}x  3 ={:^5} \n {:^3}x  4 ={:^5} \n {:^3}x  5 ={:^5} \n {:^3}x  6 ={:^5} \n {:^3}x  7 ={:^5} \n {:^3}x  8 ={:^5} \n {:^3}x  9 ={:^5} \n {:^3}x 10 ={:^5}'. format(n, n1, n, n2, n, n3, n, n4, n, n5, n, n6, n, n7, n, n8, n, n9, n, n10))