#Write a program that reads the names, ages, and genders of 4 people. At the end of the program, display: the average age of the group, the name of the oldest man, and how many women are under 20.
m = 0
o = ''
b = 0
p = 0
t = ''
for c in range(1, 5):
    n = str(input('The name of the {}ª person is: '.format(c)))
    a = int(input('The age of the {}ª person is: '.format(c)))
    g = str(input('The gender (male/female) of the {}ª person is: '.format(c))).lower()
    m = (m + a)/4
    if c == 1:
        b = a
    if g == 'male':
        if a > b:
            t = n
    if g == 'female' and a < 20:
        p += 1
print('The average of the ages is {:.2f}\nThe name of the eldest man is {}\n{} women are under 20 years old'.format(m, t, p))