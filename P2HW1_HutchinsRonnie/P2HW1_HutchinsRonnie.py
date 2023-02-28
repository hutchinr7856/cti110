# This program calculates and display travel expenses
#2-28-2023
#CTI-110 P2HW1-Travel Expense
#Ronnie Hutchins




print("This program calculates and display travel expenses")
print()
Budget = float(input("Enter Budget: "))
print()
name = input("Enter your travel destination: ")
print()
Fuel = float(input("How much do you think you will spend on Fuel? "))
print()
Accommodation=float(input("How much will you need for Accommodation? "))
print()
Food=float(input("How much do you need for Food? "))
print()
print()
print("-"*12, "Travel Expenses", 12*'-')
print("Location:               ", name)
print("Initial Budget:            $" + str (Budget) + "")
print("Fuel:                             $" + str (Fuel) + "")
print("Accommodation:      $" + str (Accommodation) + "")
print("Food:                           $" + str (Food) + "")
print()
balance = Budget - Fuel - Food - Accommodation
print("Remaining Balance: $" + str (balance) + "")
