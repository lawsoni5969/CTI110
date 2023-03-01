# A program to calculate and display travel expenses relating to a budget
# 2/28/2023
# CTI-110 P2HW1 - Travel
# Isaac Lawson
#
# Psuedocode:
#
# program start
# prompt user for budget(float)
# prompt user for destination(string)
# prompt user for gasCost(float)
# prompt user for hotelCost(float)
# prompt user for foodCost(float)
# calculate totalExpenses(float) by adding gasCost + hotelCost + foodCost
# print totalExpenses
# calculate and display remaining balance by subtracting expenses from budget
# display remaining balance
# prompt user to continue
# program end
#
print('\n--------Travel Expense Calculator--------\n')
initial_budget = float(input('Enter your budget: '))
travel_destination = input('Enter your travel destination: ')
gas_expenses = float(input('Enter your estimated gas expenses: '))
hotel_expenses = float(input('Enter your estimated hotel expenses: '))
food_expenses = float(input('Enter your estimated food expenses: '))
total_expenses = float(gas_expenses + hotel_expenses + food_expenses)
remain_balance = float(initial_budget - total_expenses)
print('\n------------Estimated Expenses-----------')
print('Destination:\t\t', travel_destination)
print('Budget:\t\t\t', f'${initial_budget:.1f}')
print('Gas:\t\t\t', f'${gas_expenses:.1f}')
print('Hotel:\t\t\t', f'${hotel_expenses:.1f}')
print('Food:\t\t\t', f'${food_expenses:.1f}')
print('Total Expenses:\t\t', f'${total_expenses:.1f}')
print('-----------------------------------------\n')
print('Remaining Balance:\t', f'${remain_balance:.1f}')
input('\nPress Enter to Continue... [ENTER]')
