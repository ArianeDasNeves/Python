#Write a program that reads the lengths of three lines and tells the user whether or not they can form a triangle.
r = float(input('What is the length of the r line segment?: '))
s = float(input('What is the length of the s line segment?: '))
t = float(input('What is the length of the t line segment?: '))
if (r + s)> t and (r + t) > s and (s + t) > r:
    print('These segments can form a triangle')
else:
    print('These segments can not form a triangle')
