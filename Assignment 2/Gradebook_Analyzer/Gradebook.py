"""
GradeBook Analyzer
Author: <Rakshit Yadav>
Date: <15th November 2025>
Course: Programming for Problem Solving Using Python
Assignment: GradeBook Analyzer Mini Project
"""

import csv
import statistics

# Task 2: Load Data (Manual or CSV)

def manual_input():
    marks = {}
    n = int(input("Enter number of students: "))
    for _ in range(n):
        name = input("Enter student name: ")
        score = float(input("Enter marks: "))
        marks[name] = score
    return marks


def load_csv():
    marks = {}
    filename = input("Enter CSV filename (example: data.csv): ")

    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)       # Skip header row
            for row in reader:
                if len(row) >= 2:
                    marks[row[0]] = float(row[1])
        print("CSV Loaded Successfully!")
    except FileNotFoundError:
        print("File not found. Try again.")
    return marks


# Task 3: Statistical Functions

def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    return statistics.median(marks_dict.values())

def find_max_score(marks_dict):
    max_student = max(marks_dict, key=marks_dict.get)
    return max_student, marks_dict[max_student]

def find_min_score(marks_dict):
    min_student = min(marks_dict, key=marks_dict.get)
    return min_student, marks_dict[min_student]


# Task 4: Grade Assignment

def assign_grades(marks_dict):
    grades = {}

    for name, score in marks_dict.items():
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        elif score >= 40:
            grade = "E"
        else:
            grade = "F"

        grades[name] = grade

    return grades


def grade_distribution(grades):
    dist = {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0}
    for g in grades.values():
        dist[g] += 1
    return dist


# Task 5: Pass/Fail Using List Comprehension

def pass_fail_filter(marks_dict):
    passed = [name for name, score in marks_dict.items() if score >= 40]
    failed = [name for name, score in marks_dict.items() if score < 40]
    return passed, failed



# Task 6: Display Table

def print_result_table(marks_dict, grades):
    print("\n---------------------------------------------")
    print("Name\t\tMarks\tGrade")
    print("---------------------------------------------")

    for name in marks_dict:
        print(f"{name:15} {marks_dict[name]:<10} {grades[name]}")

    print("---------------------------------------------\n")


# Main CLI Loop

def main():
    print("\n===== GRADEBOOK ANALYZER =====")
    print("1. Manual Input")
    print("2. Load CSV")
    print("3. Exit")

    while True:
        choice = input("\nChoose an option: ")

        if choice == "1":
            marks = manual_input()
        elif choice == "2":
            marks = load_csv()
        elif choice == "3":
            print("Exiting GradeBook Analyzer...")
            break
        else:
            print("Invalid option. Try again.")
            continue

        if not marks:
            print("No data found. Try again.")
            continue

        # Task 3 – Statistics
        avg = calculate_average(marks)
        med = calculate_median(marks)
        max_name, max_score = find_max_score(marks)
        min_name, min_score = find_min_score(marks)

        print("\n===== STATISTICAL SUMMARY =====")
        print(f"Average Marks: {avg:.2f}")
        print(f"Median Marks: {med}")
        print(f"Top Scorer: {max_name} ({max_score})")
        print(f"Lowest Scorer: {min_name} ({min_score})")

        # Task 4 – Grade assignment
        grades = assign_grades(marks)
        dist = grade_distribution(grades)
        print("\n===== GRADE DISTRIBUTION =====")
        for grade, count in dist.items():
            print(f"{grade}: {count}")

        # Task 5 – Pass/Fail
        passed, failed = pass_fail_filter(marks)
        print("\n===== PASS / FAIL SUMMARY =====")
        print(f"Passed ({len(passed)}): {passed}")
        print(f"Failed ({len(failed)}): {failed}")

        # Task 6 – Result Table
        print_result_table(marks, grades)

        again = input("Run again? (y/n): ").lower()
        if again != "y":
            print("Thank you for using GradeBook Analyzer!")
            break


if __name__ == "__main__":
    main()