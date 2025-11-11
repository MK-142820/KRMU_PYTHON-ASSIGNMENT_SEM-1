"""
------------------------------------------------------------
GradeBook Analyzer
Course: Programming for Problem Solving using Python
Student Name: Manoj Kumar
Roll No: 2501730119
Date: 10/11/2025
------------------------------------------------------------
Description:
A CLI-based GradeBook Analyzer that allows users to input or 
import student marks, perform statistical analysis, assign 
grades, and display summaries in a formatted table.
------------------------------------------------------------
"""

import csv
import statistics

# ------------------ Task 1: Project Setup ------------------

def print_menu():
    print("\n===== GradeBook Analyzer =====")
    print("1. Enter student data manually")
    print("2. Load student data from CSV")
    print("3. Exit")
    print("==============================")

print("Welcome to the GradeBook Analyzer!")
print_menu()


# ------------------ Task 2: Data Entry or CSV Import ------------------

def manual_entry():
    marks = {}
    n = int(input("Enter number of students: "))
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        score = float(input(f"Enter marks for {name}: "))
        marks[name] = score
    return marks

def load_from_csv(filename):
    marks = {}
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) >= 2:
                    marks[row[0]] = float(row[1])
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
    return marks


# ------------------ Task 3: Statistical Analysis Functions ------------------

def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    return statistics.median(marks_dict.values())

def find_max_score(marks_dict):
    return max(marks_dict.values())

def find_min_score(marks_dict):
    return min(marks_dict.values())


# ------------------ Task 4: Grade Assignment and Distribution ------------------

def assign_grades(marks_dict):
    grades = {}
    for name, score in marks_dict.items():
        if score >= 90:
            grades[name] = 'A'
        elif score >= 80:
            grades[name] = 'B'
        elif score >= 70:
            grades[name] = 'C'
        elif score >= 60:
            grades[name] = 'D'
        else:
            grades[name] = 'F'
    return grades

def grade_distribution(grades):
    dist = {'A':0, 'B':0, 'C':0, 'D':0, 'F':0}
    for g in grades.values():
        if g in dist:
            dist[g] += 1
    return dist


# ------------------ Task 5: Pass/Fail Filter ------------------

def pass_fail_list(marks_dict):
    passed_students = [name for name, score in marks_dict.items() if score >= 40]
    failed_students = [name for name, score in marks_dict.items() if score < 40]
    return passed_students, failed_students


# ------------------ Task 6: Results Table and User Loop ------------------

def display_results(marks_dict, grades):
    print("\n------------------ Student Grade Report ------------------")
    print(f"{'Name':<15}{'Marks':<10}{'Grade':<10}")
    print("-" * 40)
    for name in marks_dict:
        print(f"{name:<15}{marks_dict[name]:<10}{grades[name]:<10}")
    print("-" * 40)

def analyze_data(marks):
    print("\n----- Statistical Summary -----")
    print(f"Average Marks: {calculate_average(marks):.2f}")
    print(f"Median Marks : {calculate_median(marks):.2f}")
    print(f"Highest Score: {find_max_score(marks)}")
    print(f"Lowest Score : {find_min_score(marks)}")

    grades = assign_grades(marks)
    dist = grade_distribution(grades)

    print("\n----- Grade Distribution -----")
    for grade, count in dist.items():
        print(f"{grade}: {count} students")

    passed, failed = pass_fail_list(marks)
    print("\n----- Pass/Fail Summary -----")
    print(f"Passed ({len(passed)}): {', '.join(passed)}")
    print(f"Failed ({len(failed)}): {', '.join(failed)}")

    display_results(marks, grades)


# ------------------ CLI Loop ------------------

while True:
    print_menu()
    choice = input("Enter your choice (1-3): ").strip()

    if choice == '1':
        data = manual_entry()
        analyze_data(data)

    elif choice == '2':
        filename = input("Enter CSV filename (with .csv extension): ")
        data = load_from_csv(filename)
        if data:
            analyze_data(data)

    elif choice == '3':
        print("Exiting GradeBook Analyzer. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")