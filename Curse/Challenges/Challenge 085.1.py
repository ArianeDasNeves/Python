#Write a program that declares a 3×3 array and fills it with values entered from the keyboard. At the end, display the array on the screen, formatted correctly.

l = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for r in range(0, 3):
        l[c][r] = int(input(f'Enter a number for the position [{c}/{r}]: '))
for c in range(0, 3):
    for r in range(0, 3):
        print(f'[{l[c][r]:^5}]', end='')
    print(end = '\n')