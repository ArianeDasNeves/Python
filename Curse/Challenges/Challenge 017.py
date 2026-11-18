#A teacher wants to randomly select one of his four students to erase the board. Write a program to help him by reading the students' names and displaying the name of the selected student on the screen.
import random
a = input('Student 1: ')
b = input('Student 2: ')
c = input('Student 3: ')
d = input('Student 4: ')
e =(a, b, c, d)
f = random.sample(e, 1)
print('The student who is clean the board is: {}'.format(f))