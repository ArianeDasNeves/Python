#Write a program that takes a single tuple containing product names and their respective prices, in sequence. At the end, display a list of prices, organizing the data in tabular form.



#p = ['carne', 33, 'Macarrão', 2, 'Feijão', 8, 'Salmão', 56, 'Amaciante', 17, '1Kg de Laranja', 7]
#for c in range (0, len(p), 2):
#    print(f'{p[c]:.<14}{'.'*20}R${p[c+1]:0>5.2f}')
total = []
c = 0
an = 0
while True:
    n = str(input('What is the name of the product?: ')).capitalize()
    p = float(input('What is the price of the product?: R$'))
    c += 1
    total.append(n)
    total.append(p)
    q = str(input('DO you want to continue? [S]/[N]: ')).upper().strip()
    if q != 'S' and q != 'N':
        q = str(input('DO you want to continue? [S]/[N]: ')).upper().strip()
    if q == 'N':
        break
for c in range (0, len(total), 2):
    print(f'{total[c]:.<14}{'.'*20}R${total[c+1]:>6.2f}')