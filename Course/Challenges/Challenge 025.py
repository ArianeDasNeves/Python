#Write a program that reads a sentence from the keyboard and displays how many times the letter “A” appears, at what position it first appears, and at what position it last appears.
#The second attempt
phrase = input('Enter a phrase: ').strip()
print('There are {} letters A in the sentence'.format(phrase.lower().count('a')))
print('The first letter A appeared in the position {}'.format(phrase.lower().find('a')+1))
print('The last letter A appeared in the position {}'.format(phrase.lower().rfind('a')+1))
