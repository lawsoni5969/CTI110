# A program that takes a number grade, determines average, and displays letter grade for average.
# 3/18/2023
# CTI-110 P3HW1 - Debugging
# Isaac Lawson

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

lowG = min(grades)
highG = max(grades)
sumG = sum(grades)
avgG = sumG / len(grades)

# print results

print('\n------------Results------------')
print('Lowest Grade:\t', f'{lowG:.1f}')
print('Highest Grade:\t', f'{highG:.1f}')
print('Sum of Grades:\t', f'{sumG:.1f}')
print('Average:\t', f'{avgG:.2f}')
print('----------------------------------------')

# determine letter grade for average

if avgG >= 90:
    print('Your grade is: A')
elif avgG >= 80:
    print('Your grade is: B')
elif avgG >= 70:
    print('Your grade is: C')
elif avgG >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')





