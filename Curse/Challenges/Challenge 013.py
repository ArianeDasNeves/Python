#Write a program that asks for the number of kilometers traveled by a rental car and the number of days it was rented. Calculate the total cost, given that the car costs R$60 per day and R$0.15 per kilometer traveled.
day = float(input('How many days did you rent the car? '))
distance = float(input('How many kilometers did you travel? '))
c = day*60 + distance*(0.15)
print('You will to pay:U${}'.format(c))
