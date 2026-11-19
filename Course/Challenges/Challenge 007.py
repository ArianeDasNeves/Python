#Write a program that reads the width and height of a wall in meters, calculates its area and the amount of paint needed to paint it, given that each liter of paint covers an area of 2 square meters.
h = float(input('What is the wall height? '))
l = float(input('What is the wall lenght? '))
a = h*l
print('The area of the wall is {} square meters'.format(a))
q = a/2
print('The aumont of ink required is {} liters'.format(q))
