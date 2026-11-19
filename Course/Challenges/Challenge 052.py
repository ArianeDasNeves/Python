#Write a program that reads any sentence and determines whether it is a palindrome, ignoring spaces.
n = str(input('Write a sentence: ')).upper().split()
na = ''.join(n)
i = ''
nb = (na.replace('Á', 'A').replace('À', 'A').replace('Â', 'A').replace('Ã', 'A').replace('É', 'E').replace('È', 'E').replace('Ê', 'E').replace('Í', 'I').replace('Ì', 'I').replace('Î', 'I').replace('Ó', 'O').replace('Ò', 'O').replace('Ô', 'O').replace('Õ', 'O').replace('Ú', 'U').replace('Ù', 'U').replace('Û', 'U').replace('Ç', 'C').replace('.', '').replace(',', '').replace(';', '').replace(':', '').replace('!', '').replace('?', '').replace('"', '').replace("'", '').replace('-', '').replace('%', '').replace('&', '').replace('~', '').replace('`', '').replace('^', ''))
l = len(nb)
print('\n{}'.format('=-'*20))
for c in range(0, l):
    print(nb[c], end='')
print('\n{}'.format('=-'*20))
for a in range(l-1, -1, -1):
    print(nb[a], end='')
    i += nb[a]
print('\n{}'.format('=-'*20))
if nb == i:
    print('\nThis is a Palindrome')
else:
    print('\nThis is not a Palindrome')