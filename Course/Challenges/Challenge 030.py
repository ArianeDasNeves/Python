#Write a program that asks for the distance of a trip in kilometers. Calculate the fare, charging R$0.50 per kilometer for trips up to 200 kilometers and R$0.45 for longer trips.
d = float(input('Enter the distance of the trip in kilometers: '))
if d <= 200:
    print('The ticket of the trip is: R${}'.format((d*0.5)))
else:
    print('The ticket of the trip is: R${}'.format((d*0.45)))
