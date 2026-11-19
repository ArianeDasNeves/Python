# Write a program that reads the name and price of several products. The program should ask the user whether they want to continue or not. At the end, display:
# A) the total amount spent on the purchase.
# B) how many products cost more than R$1,000.
# C) the name of the cheapest product.
s = b = c = d = 0
cheaper = ''
while True:
    print('-='*20)
    n = str(input('What is the name of the product?: ')).upper().strip()
    p = float(input('What is the price of the product?: '))
    q = str(input('Do you want to continue? [Y/N]: ')).upper().strip()
    while q != 'Y' and q != 'N':
        q = str(input('Do you want to continue? [Y/N]: ')).upper().strip()
    d += 1
    if d == 1:
        b = p
        cheaper = n
    else:
        if p < b:
            cheaper = n
            b = p
    if p > 1000:
        c += 1
    s += p
    if q == 'N':
        break
print(f'The total cost of the purchase is R${s}\n{c} products cost more than R$1.000\nThe cheaper product is {cheaper}')
