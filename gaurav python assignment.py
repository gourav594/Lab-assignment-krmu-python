# Daily Calorie Tracker CLI
# Author: Gourav
# Date: 07-10-2025
# Project: Mini Project Assignment - Daily Calorie Tracker

print("Welcome to the Daily Calorie Tracker!")
print("You can log your meals and track calories easily.\n")

# Lists to store meals and calories
meal_names = []
calorie_amounts = []

# Ask user how many meals
num_meals = int(input("How many meals do you want to enter today? "))

# Get meal names and calories
for i in range(num_meals):
    meal = input(f"Enter name of meal {i+1}: ")
    calories = float(input(f"Enter calories for {meal}: "))
    meal_names.append(meal)
    calorie_amounts.append(calories)

# Total and average calories
total_calories = sum(calorie_amounts)
average_calories = total_calories / num_meals

# Daily calorie limit
daily_limit = float(input("\nEnter your daily calorie limit: "))

# Check if limit exceeded
if total_calories > daily_limit:
    print("\n⚠️ You have exceeded your daily calorie limit!")
else:
    print("\n✅ You are within your daily calorie limit.")

# Print summary
print("\n======== Daily Calorie Summary ========")
print("Meal Name\tCalories")
print("-------------------------------")
for meal, cal in zip(meal_names, calorie_amounts):
    print(f"{meal}\t\t{cal}")
print("-------------------------------")
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{average_calories:.2f}")
print("======================================")
