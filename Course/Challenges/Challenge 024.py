#Write a program that reads a sentence from the keyboard and displays how many times the letter “A” appears, at what position it first appears, and at what position it last appears.
#The first attempt
phrase = input('Enter a phrase: ')
print('The letter A appears {} times'.format(phrase.lower().count('a')))
print('The letter a appears for the first time in the position: {}'.format(phrase.lower().find('a')))
print('The letter a appears for the last time in the position: {}'.format(phrase.lower().find('a')))