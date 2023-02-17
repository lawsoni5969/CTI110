# A program to calculate and display travel expenses relating to a budget
# 2/16/2023
# CTI-110 P1HW2 - Travel Expense
# Isaac Lawson
#
# Psuedocode:
#
# program start
# prompt user for budget(int)
# prompt user for destination(string)
# prompt user for gasCost(int)
# prompt user for hotelCost(int)
# prompt user for foodCost(int)
# calculate totalExpenses(int) by adding gasCost + hotelCost + foodCost
# print totalExpenses
# calculate and display leftoverBalance by subtracting totalExpenses from budget
# prompt user to continue
# program end
#
print('\n-------------Travel Expense Calculator------------\n')
initial_budget = int(input('Enter your budget: '))
travel_destination = input('Enter your travel destination: ')
gas_expenses = int(input('Enter your estimated gas expenses: '))
hotel_expenses = int(input('Enter your estimated hotel expenses: '))
food_expenses = int(input('Enter your estimated food expenses: '))
total_expenses = int(gas_expenses + hotel_expenses + food_expenses)
print('\n----------------Estimated Expenses----------------\n')
print('Destination:\t\t', travel_destination)
print('Budget:\t\t\t', initial_budget)
print('\nGas:\t\t\t', gas_expenses)
print('Hotel:\t\t\t', hotel_expenses)
print('Food:\t\t\t', food_expenses)
print('\nTotal Expenses:\t\t', total_expenses)
print('Remaining Balance:\t', initial_budget - total_expenses)
input('\n\nPress Enter to Continue... [ENTER]')
