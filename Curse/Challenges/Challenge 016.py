#Write a program that reads any angle and displays the sine, cosine, and tangent of that angle on the screen.
import math
a = int(input('Enter a angle: '))
print('The sine of the {} is {:.2f} and the cosine is {:.2f}'.format(a, math.sin(math.radians(a)), math.cos(math.radians(a))))
