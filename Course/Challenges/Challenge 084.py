#Write a program in which the user can enter seven numeric values and store them in a single list that keeps even and odd values separate. Finally, display the even and odd values in ascending order.
l = [[], []]
for c in range (0, 7):
    n = int(input('Enter a number: '))
    if n % 2 == 0:
        l[0].append(n)
    else:
        l[1].append(n)
    l[0].sort()
    l[1].sort()
print(f'The even numbers are: {l[0]}\nThe odd numbers are: {l[1]}')