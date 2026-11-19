#Write a program that reads a person's full name and then displays the first and last names separately.
name = str(input('Write your name: ')).strip()
n = name.split()
print('Your first name is: {}'.format(n[0]))
print('Your last name is: {}'.format(n[len(n)-1]))
