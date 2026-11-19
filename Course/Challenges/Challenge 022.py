#Write a program that reads the name of a city and determines whether or not it begins with the word “SANTO.”

city = input('Write a name of a city: ').strip()
print('st' in city.lower().split()[0])
print('san' in city.lower().split()[0])
print('santa' in city.lower().split()[0])
