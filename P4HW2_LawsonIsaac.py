# CTI-110
# P4HW2 - Salary Calculator
# Isaac Lawson
# 4/18/2023
#
# Psuedocode:
#
# start program
# Begin loop with no native exit condition
# request employee's name and store in a variable (str)
# if empName is equal to "Done", break the loop and end program
# else
# request hours worked and store in a variable (float)
# request employee's pay rate and store in a variable (float)
# print hours worked
# print pay rate
# calculate overtime by subtracting 40 form hours worked and print the remainder
# calculate overtime pay using the following formula (payRate * 1.5) * otHours
# print calculated overtime pay
# calculate regular pay using the following formula (hoursWorked - otHours) * payRate
# print calculated regular pay
# print gross pay by adding regular pay and overtime pay and displaying the result
# loop returns to start
#

while 0 == 0:
    empName = str(input("\n\nEnter employee's name or \"Done\" to terminate: "))
    if empName == "Done":
        break
    hoursWorked = float(input("Enter number of hours worked: "))
    payRate = float(input("Enter employee's pay rate: "))
    if hoursWorked > 40:
        otHours = hoursWorked - 40
    else:
        otHours = 0
    otPay = (payRate * 1.5) * otHours
    regPay = (hoursWorked - otHours) * payRate
    grossPay = regPay + otPay
    print("----------------------------------")
    print("Employee name:\t", empName)
    print("\nHours Worked       Pay Rate       OverTime       OverTime Pay       RegHour Pay       Gross Pay")
    print("--------------------------------------------------------------------------------------------------------")
    print(f'{hoursWorked:<19.1f}${payRate:<14.1f}{otHours:<15.1f}${otPay:<18.2f}${regPay:<17.2f}${grossPay:.2f}')
