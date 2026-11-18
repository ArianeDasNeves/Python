#Write a program that reads the birth years of seven people. At the end, display how many people are still minors and how many are adults.
import datetime
d = datetime.date.today()
print('This is the year: {}'.format(d.year))
b = 0
a = 0
for c in range(0, 7):
    n = int(input('What year were you born in?'))
    if d.year - n >= 21:
        a += 1
    if d.year - n < 21:
        b +=1
print('{} people have already reached the age of majority, and {} have not yet'.format(a, b))