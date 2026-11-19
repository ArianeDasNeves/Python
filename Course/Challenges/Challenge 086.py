# Expand on the previous challenge by displaying the following at the end:
# A) The sum of all even values entered.
# B) The sum of the values in the third column.
# C) The largest value in the second row.
l = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
e = 0
s = 0
for c in range(0, 3):
    for r in range(0, 3):
        l[c][r] = int(input(f'Enter a number for the position [{c}/{r}]: '))
        if l[c][r] % 2 == 0:
            e += l[c][r]
        if r == 2:
            s += l[c][r]
for c in range(0, 3):
    for r in range(0, 3):
        print(f'[{l[c][r]:^5}]', end='')
    print(end = '\n')
print(f'The sum of the even numbers is: [{e}]')
print(f'The sum of the all values in the third column is: [{s}]')
print(f'The highest value in the second line is: [{max(l[1])}]')