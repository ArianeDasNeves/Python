#Write a program that reads a car's speed. If it exceeds 80 km/h, display a message stating that the driver has been fined. The fine will be R$7.00 for every kilometer over the speed limit.
v = float(input('What is the velocity of the car?: '))
if v > 80.0:
    print('You received a traffic ticket')
    print('You will pay: R${}'.format((v - 80)*7))
else:
    print('Have a nice day, drive safely')
