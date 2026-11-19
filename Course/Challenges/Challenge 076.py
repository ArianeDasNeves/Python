#Write a program that takes a tuple containing several words (do not use accents). Then, for each word, display its vowels.
t = ['caderno', 'margarida', 'vinhedo', 'bonito', 'laranja', 'violoncelo', 'lapis']
for c in t:
    print(f'\nNa palavra {c} temos: ', end = '')
    for l in c:
        if l.lower() in 'aeiou':
            print(l, end = ' ')