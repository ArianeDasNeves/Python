#The same teacher from Challenge 17 wants to randomly determine the order in which the students will present their projects. Write a program that reads the names of the four students and displays the randomly determined order.
import random
a = input('Student 1: ')
b = input('Student 2: ')
c = input('Student 3: ')
d = input('Student 4: ')
e = [a, b, c, d]
random.shuffle(e)
print('The order to present is: {}'.format(e))
