# Project: Daily Calorie Tracker
# Author: [Rakshit Yadav]
# Roll No: [2501730016]
# Date: [3 November 2025]
# Description: A CLI tool to track daily calorie intake,
#              compare with personal limits, and save logs.



import datetime

# Task 1: Setup & Introduction
print("\nWelcome to the Daily Calorie Tracker!")
print("This tool helps you log your meals, track total calories, and compare them with your daily calorie limit.\n")

#  Task 2: Input & Data Collection 
meals = []
calories = []

num_meals = int(input("How many meals do you want to enter today? "))

for i in range(num_meals):
    meal_name = input(f"\nEnter the name of meal #{i+1}: ")
    calorie_amount = float(input(f"Enter calories for {meal_name}: "))
    meals.append(meal_name)
    calories.append(calorie_amount)

# 
#  Task 3: Calorie Calculations 

total_calories = sum(calories)
average_calories = total_calories / len(calories)

daily_limit = float(input("\nEnter your daily calorie limit: "))

# 
#  Task 4: Exceed Limit Warning System

if total_calories > daily_limit:
    status_message = "⚠️ You have exceeded your daily calorie limit!"
else:
    status_message = "✅ You are within your daily calorie limit. Good job!"

# 
#  Task 5: Neatly Formatted Output 

print("\n" + "-" * 40)
print("Meal Name\t\tCalories")
print("-" * 40)

for meal, cal in zip(meals, calories):
    print(f"{meal:<16}\t{cal:.2f}")

print("-" * 40)
print(f"Total:\t\t\t{total_calories:.2f}")
print(f"Average per meal:\t{average_calories:.2f}")
print(status_message)
print("-" * 40)

# 
#  Task 6 (Bonus): Save Session Log to File

save_choice = input("\nDo you want to save this session report? (yes/no): ").strip().lower()

if save_choice == "yes":
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"calorie_log_{timestamp}.txt"

    with open(filename, "w") as file:
        file.write("Daily Calorie Tracker Log\n")
        file.write(f"Date & Time: {datetime.datetime.now()}\n\n")
        file.write("Meal Name\t\tCalories\n")
        file.write("-" * 40 + "\n")
        for meal, cal in zip(meals, calories):
            file.write(f"{meal:<16}\t{cal:.2f}\n")
        file.write("-" * 40 + "\n")
        file.write(f"Total:\t\t\t{total_calories:.2f}\n")
        file.write(f"Average per meal:\t{average_calories:.2f}\n")
        file.write(status_message + "\n")
    
    print(f"\n📁 Session saved successfully to {filename}")
else:
    print("\nSession not saved. Goodbye!")


