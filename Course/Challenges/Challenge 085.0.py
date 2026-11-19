#Write a program that declares a 3×3 array and fills it with values entered from the keyboard. At the end, display the array on the screen, formatted correctly.




# l = [[[], [], []], [[], [], []], [[], [], []]]
# for c in range(0, 3):
#     l[0].append(int(input(f'Enter a number for the position [0, {c}]: ')))
# for c in range(0, 3):
#     l[1].append(int(input(f'Enter a number for the position [1, {c}]: ')))
# for c in range(0, 3):
#     l[2].append(int(input(f'Enter a number for the position [2, {c}]: ')))
# print(f'[{l[0][0]:^5}][{l[0][1]:^5}][{l[0][2]:^5}]\n[{l[1][0]:^5}][{l[1][1]:^5}][{l[1][2]:^5}]\n[{l[2][0]:^5}][{l[2][1]:^5}][{l[2][2]:^5}]')

# l = [[[], [], []], [[], [], []], [[], [], []]]
# for i in range(0, 3):
#     for c in range(0, 3):
#         l[i][c].append((input(f'Enter a number for the position [{i}, {c}]: ')))
# for i in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{l[i][c][0]:^5}]', end='' if c < 2 else '\n')

l = [[0,0,0], [0,0,0], [0, 0, 0]]
for i in range(0, 3):
    for c in range(0, 3):
        l[i][c] = int(input(f'Enter a number for the position [{i}, {c}]: '))
for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{l[i][c]:^5}]', end='' if c < 2 else '\n')

