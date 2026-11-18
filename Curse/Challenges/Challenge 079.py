#Write a program where the user can enter five numeric values and add them to a list, placing them in the correct position (without using sort()). Finally, display the sorted list on the screen.
l = []
for c in range(0, 5):
    n = int(input('Enter a number: '))
    if c == 0 or n > l[len(l)-1]:
        l.append(n)
    else:
        if n < l[0]:
            l.insert(0, n)
        else:
            p = 0
            while True:
                if n <= l[p]:
                    l.insert(p, n)
                    break
                p += 1
                print(p)
    print(l)
print(l)