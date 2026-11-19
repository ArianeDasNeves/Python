#Write a program that reads a young person's year of birth and, based on their age, indicates whether they are still eligible to enlist in the military,
# whether it is exactly the right time to enlist, or whether the enlistment deadline has already passed. Your program should also display how much time is left until the deadline or how much time has elapsed since the deadline.
import datetime
from dateutil.relativedelta import relativedelta
a = int(input('What is your year of birth?:'))
b = int(input('What is your month of birth?:'))
c = int(input('What is your day of birth?:'))
d = datetime.date.today()
e = datetime.date(a, b, c)
f = relativedelta(d,e)
g = datetime.date(a+18, 11, c-1)
h = relativedelta(d,g)
i = datetime.date(a+18, b, c)
j = relativedelta(d, i)
if h.years<0:
    h.years = -h.years
if h.months<0:
    h.months = -h.months
if h.days<0:
    h.days = -h.days
if j.years<0:
    j.years = -j.years
if j.months<0:
    j.months = -j.months
if j.days<0:
    j.days = -j.days
print('Your age is: {} years, {} months and {} days'.format(f.years, f.months, f.days))
if f.years == 18:
    print('You have to register for mandatory military service')
elif f.years < 18:
    print('It is not time to register for mandatory military service yet; there are still: {} years, {} months and {} days'.format(j.years, j.months, j.days))
elif f.years > 18:
    print('It is past time to register for mandatory military service; it has been {} years, {} months and {} days past the deadline'.format(h.years, h.months, h.days))




