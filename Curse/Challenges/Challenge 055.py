#Write a program that reads the weights of five people. At the end, display the highest and lowest weights read.
a = 0
b = 0
for c in range(1, 6):
    p = float(input('What is the body weight of the {}ª person? '.format(c)))
    if c == 1:
        a = p
        b = p
    if p > a:
        a = p
    if p < b :
        b = p
print('The biggest weight is {} and the smallest weight is {}'.format(a, b))

