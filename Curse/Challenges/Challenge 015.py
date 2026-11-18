#Write a program that reads the lengths of the opposite and adjacent sides of a right triangle. Calculate and display the length of the hypotenuse.
import math
side_a = float(input('Enter a lenght adjacent side: '))
side_b = float(input('Enter a lenght opposite side: '))
print('The hypotenuse is: {:.2f}'.format(math.hypot(side_a, side_b)))



