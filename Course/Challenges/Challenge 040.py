# The National Swimming Confederation needs a program that reads an athlete’s year of birth and displays their category based on age:
#
#
# – Up to 9 years old: CHILD
#
#
# – Up to 14 years old: YOUTH
#
#
# – Up to 19 years old: JUNIOR
#
#
# – Up to 25 years old: SENIOR
#
#
# – Over 25 years old: MASTER
import datetime
from dateutil.relativedelta import relativedelta
a = int(input('What is your year of birth?:'))
b = int(input('What is your month of birth?:'))
c = int(input('What is your day of birth?:'))
d = datetime.date.today()
e = datetime.date(a, b, c)
f = relativedelta(d,e)
g = datetime.date(a, b, c-1)
h = relativedelta(d, g)
print('Your age is: {} years, {} months and {} days'.format(f.years, f.months, f.days))
if h.years <= 9 and h.months <= 11:
    print('His category in the National Swimming Confederation is: CHILD')
if h.years <=14 and h.months <=11:
    print('His category in the National Swimming Confederation is: YOUTH')
if h.years <=19 and h.months <=11:
    print('His category in the National Swimming Confederation is: JUNIOR')
if h.years <=20 and h.months <=11:
    print('His category in the National Swimming Confederation is: SENIOR')
if h.years >20:
    print('His category in the National Swimming Confederation is: MASTER')