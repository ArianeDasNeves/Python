# Redo CHALLENGE 34 on triangles, adding a feature that shows what type of triangle will be formed:
#
#
# – EQUILATERAL: all sides are equal
#
#
# – ISOSCELES: two sides are equal, one is different
#
#
# – SCALENE: all sides are different
r = float(input('What is the length of the r line segment?: '))
s = float(input('What is the length of the s line segment?: '))
t = float(input('What is the length of the t line segment?: '))
if (r + s)> t and (r + t) > s and (s + t) > r:
    print('These segments can form a triangle')
    if r==t==s:
        print('This is a equilateral triangle')
    if r==t or r==s or s==t:
        print('This is a isosceles triangle')
    if r!=s!=t:
        print('This is a scalene triangle')
else:
    print('These segments can not form a triangle')
