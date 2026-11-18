#Write a program that reads a number from 0 to 9999 and displays each digit separately on the screen.


# number = str(input('Enter a number from 0 to 9999: '))
# print('Unit:', number[3])
# print('Tens:', number[2])
# print('Hundreds:', number[1])
# print('Thousands:', number[0])

number = int(input('Enter a number from 0 to 9999: '))
print('Unit: {}'.format(number % 10))
print('Tens: {}'.format((number // 10) % 10))
print('Hundreds: {}'.format((number // 100) %10))
print('Thousands: {}'.format((number // 1000) % 10))

