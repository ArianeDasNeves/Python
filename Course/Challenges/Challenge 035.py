#Write a program to approve a bank loan for the purchase of a house. Ask for the price of the house, the buyer's salary, and the number of years over which the loan will be repaid. The monthly payment cannot exceed 30% of the salary; otherwise, the loan will be denied.
a = float(input('What is the value of the property?: US$'))
b = float(input('What is your salary?: US$'))
c = float(input('How many years do you plan to take to pay it off?: '))
d = a/(c*12)
if (d/b) < 0.3:
    print('Your bank loan has been approved.')
    print('The monthly instalment is: US${:.2f}'.format(d))
else:
    print('Your bank loan has been rejected.')
