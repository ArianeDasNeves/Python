#Write a program that reads a value in meters and displays it converted to centimeters and millimeters.
n = float(input('Unit Converter(meters): '))
n1 = n*100
n2 = n*1000
print('The number in centimeters is {}, The number in milimeters is {}'.format(n1, n2))
