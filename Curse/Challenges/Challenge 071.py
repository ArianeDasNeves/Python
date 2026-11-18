#Write a program that displays a fully filled-in pair with numbers written out in words, from zero to twenty. Your program should read a number from the keyboard (between 0 and 20) and display it written out in words.
c = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
while True:
    n = int(input('Choose a number from 0 to 20: '))
    if 20 < n or n < 0:
        print('-='*20)
        n = int(input('Wrong answer!!! Choose a number from 0 to 20: '))
    if 0 <= n <= 20:
        break
print('-='*20)
print('You choose the number:', c[n])
