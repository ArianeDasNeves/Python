#Write a program that reads a person's gender, but only accepts the values 'M' or 'F'. If the input is incorrect, ask the user to re-enter it until a correct value is provided.
import time
r = ''
while r != 'M' and r != 'F':
    r = str(input('What is your gender? [M/F]: ')).upper()
    if r != 'M' and r != 'F':
        time.sleep(0.5)
        print('=-'*20)
        time.sleep(0.5)
        print('Enter a correct answer [M/F]')
        time.sleep(0.5)
        print('=-' * 20)
        time.sleep(0.5)
print('End')
