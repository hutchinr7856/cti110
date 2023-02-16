# This program calculates and display travel expenses
#2-16-2023
#CTI-110 P1HW2-Travel Expense
#Ronnie Hutchins




print("This program calculates and display travel expenses")
print()
budget = float(input("Enter budget: "))
print()
name = input("Enter your travel destination: ")
print()
gas = float(input("How much do you think you will spend on gas? "))
print()
hotel=float(input("How much will you need for hotel? "))
print()
food=float(input("How much do you need for food? "))
print()
balance = budget - gas - hotel - food
print("Remaining Balance:", balance)
print()
