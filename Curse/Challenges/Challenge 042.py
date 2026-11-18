# Develop a program that reads a person’s weight and height, calculates their Body Mass Index (BMI), and displays their status according to the table below:
#
#
# – BMI below 18.5: Underweight
#
#
# – Between 18.5 and 25: Ideal Weight
#
#
# – 25 to 30: Overweight
#
#
# – 30 to 40: Obese
#
#
# – Above 40: Morbidly Obese
# Inline corrections
#
# Get real-time corrections for spelling and grammar whenever you write or edit text in your browser.


w = float(input('What is your weight(kg)? '))
h = float(input('What is your height(m)? '))
c = w/(h**2)
print('Your IMC is: {:.1f}'. format(c))
if c < 18.5:
    print('You are underweight')
elif 18.5 <= c < 25:
    print('You are at your ideal weight')
elif 25 <= c < 30:
    print('You are overweight')
elif 30 <= c < 40:
    print('You are morbidly obese')
