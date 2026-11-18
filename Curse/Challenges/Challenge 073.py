#Write a program that generates five random numbers and stores them in a tuple. Then, display the list of generated numbers and also indicate the smallest and largest values in the tuple.
import random
p = []
h = 0
s = 0
#t = [random.randint(0, 100) for i in range(0,5)]
#print(max(t), min(t))
for i in range(0,5):
    t = random.randint(0, 100)
    p.append(t)
    if i == 0:
        h = t
        s = t
    else:
        if t > h:
            h = t
        elif t < s:
            s = t
print(f'The numbers generated are: {p}\nThe highest number is: {h}\nThe lowest number is: {s}')
