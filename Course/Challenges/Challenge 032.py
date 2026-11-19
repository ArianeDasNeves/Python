#Write a program that reads three numbers and displays which one is the largest and which one is the smallest.
n1 = float(input('Enter a number: '))
n2 = float(input('Enter another number: '))
n3 = float(input('Enter another number: '))
#if n1 > n2 and n1 > n3:
    #print('The largest number is: {}'.format(n1))
    #if n2 > n3:
        #print('The smallest numer is: {}'.format(n3))
    #if n2 <n3:
        #print('The smallest number is: {}'.format(n2))
#if n2 > n1 and n2 > n3:
    #print('The largest number is: {}'.format(n2))
    #if n3 > n1:
        #print('The smallest number is: {}'.format(n1))
    #if n1 > n3:
        #print('The smallest number is: {}'.format(n3))
#if n3 > n1 and n3 > n2:
    #print('The largest number is: {}'.format(n3))
    #if n2 > n1:
        #print('The smallest number is: {}'.format(n1))
    #if n1 > n2:
        #print('The smallest number is: {}'.format(n2))
if n1 > n2 > n3:
    print('The largest number is {} and the smallest number is {}'.format(n1, n3))
if n2 > n1 > n3:
    print('The largest number is {} and the smallest number is {}'.format(n2, n3))
if n3 > n1 > n2:
    print('The largest number is {} and the smallest number is {}'.format(n3, n2))
if n2 > n3 > n1:
    print('The largest number is {} and the smallest number is {}'.format(n2, n1))
if n3 > n2 > n1:
     print('The largest number is {} and the smallest number is {}'.format(n3, n1))
if n1 > n3 > n2:
    print('The largest number is {} and the smallest number is {}'.format(n1, n2))