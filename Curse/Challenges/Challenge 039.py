# Write a program that reads two grades for a student and calculates the student’s average, displaying a message at the end based on the average:
#
#
# – Average below 5.0: FAILED
#
#
# – Average between 5.0 and 6.9: NEEDS TO TAKE A REMEDIAL COURSE
#
#
# – Average of 7.0 or higher: PASSED
note1 = float(input('Enter note: '))
note2 = float(input('Enter another note: '))
average = (note1 + note2) / 2
print('Your average is: {}'.format(average))
if average < 5.0:
    print('You failed!')
elif average >= 5.0 and average < 6.9:
    print('You need to take the make-up test.')
elif average >= 7.0:
    print('You passed the test.')
