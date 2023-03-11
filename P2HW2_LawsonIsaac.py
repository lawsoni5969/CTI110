#   CTI-110
#   P2HW2 - List
#   Isaac Lawson
#   3/9/2023
#
#   Psuedocode:
#
#   Program Start
#   Create list to store grades (grades_list)
#   request module 1 grade (float) and store in grades_list[0]
#   repeat for module 2 - 6 (float) and store in grades_list[1] - [5]
#   print lowest grade (float)
#   print highest grade (float)
#   print sum of grades (float)
#   print average of grades (float) by taking sum of grades and dividing by 6
#   program end
#
grades_list = []
grades_list.append(float(input('Enter grade for Module 1: ')))
grades_list.append(float(input('Enter grade for Module 2: ')))
grades_list.append(float(input('Enter grade for Module 3: ')))
grades_list.append(float(input('Enter grade for Module 4: ')))
grades_list.append(float(input('Enter grade for Module 5: ')))
grades_list.append(float(input('Enter grade for Module 6: ')))
print('\n------------Results------------')
gradesAvg = sum(grades_list) / 6
print('Lowest Grade: \t', f'{min(grades_list):.1f}')
print('Highest Grade: \t', f'{max(grades_list):.1f}')
print('Sum of Grades: \t', f'{sum(grades_list):.1f}')
print('Average: \t', f'{gradesAvg:.2f}')
print('----------------------------------------')
