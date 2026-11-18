#Write a program that asks for an employee's salary and calculates the amount of their raise. For salaries greater than R$1,250.00, calculate a 10% raise. For salaries less than or equal to that amount, the raise is 15%.
s = float(input('What is your salary?: '))
if s > 1250:
    print('Your new salary is US${}'.format(s*1.10))
else:
    print('Your new salary is US${}'.format(s*1.15))
