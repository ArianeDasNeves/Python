#Write a program that reads any given year and determines whether it is a leap year.
a = int(input('Enter a year: '))
if a%4==0 and a%100!=0 or a%400==0:
    print('This year is a leap year')
else:
    print('This year is not a leap year')
