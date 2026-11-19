# Create a tuple containing the top 20 teams in the Brazilian Soccer Championship standings, in order of ranking. Then display:
# a) The top 5 teams.
# b) The bottom 4 teams.
# c) Teams in alphabetical order.
# d) The position of the Chapecoense team.
c = ('Palmeiras', 'Flamengo', 'Athletico-PR', 'Fluminense', 'Cruzeiro', 'Bahia', 'Corinthians', 'Bragantino', 'Botafogo', 'Coritiba', 'Atlético-MG', 'São Paulo', 'Vitória', 'Grêmio', 'Mirassol', 'Internacional', 'Santos', 'Vasco', 'Remo', 'Chapecoense')
print('-='*30)
print(f'First place: {c[0]}\nSecond place: {c[1]}\nThird place: {c[2]}\nFourth place: {c[3]}\nFifth place: {c[4]}')
#print(f'Os 5 primeiros times são: {c[0:5]}')
print('-='*30)
#print(f'Seventeenth place: {c[16]}\nEighteenth place: {c[17]}\nNineteenth place: {c[18]}\nTwentieth place: {c[19]}')
print(f'Os 4 últimos times são: {c[-4:]}')
print('-='*30)
print(f'The teams sorted alphabetically are: {sorted(c)}')
print('-='*30)
print(f'Chapecoense is in the {c.index('Chapecoense')+1} position')