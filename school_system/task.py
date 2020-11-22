# CLASS DIARY

# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).

import json
import random
import statistics
import os


def import_data():
    with open('data.json') as json_file:
        data = json.load(json_file)
    return data


def save_data(data):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)


def calculate_average(grades):
    return statistics.mean(grades)


def calculate_att_pr(att):
    sum_total = 0
    for i in att:
        if i == 1:
            sum_total = sum_total + 1
    return sum_total/len(att)


def add_grade(data, class_index, student_index, grade):
    class_id = 'class' + str(class_index)
    student_id = 'student' + str(student_index)
    all_grades = data["school1"][class_id][student_id]["grades"]
    all_grades.append(grade)
    data["school1"][class_id][student_id]["avg"] = calculate_average(
        all_grades)


def reg_att(data, class_index, student_index, att):
    class_id = 'class' + str(class_index)
    student_id = 'student' + str(student_index)
    all_attendances = data["school1"][class_id][student_id]["attendance"]
    all_attendances.append(att)
    data["school1"][class_id][student_id]["att_pr"] = calculate_att_pr(
        all_attendances)


def add_student(data, class_index, name, surname):
    new_student = {
        "name": name,
        "surname": surname,
        "grades": [],
        "attendance": [],
        "avg": 0,
        "att_pr": 0
    }
    class_id = 'class' + str(class_index)
    student_id = 'student' + str(len(data["school1"]["class1"])+1)
    data["school1"][class_id][student_id] = new_student


def find_student(data, name, surname):
    class_index = 0
    student_id = 0
    for i in range(1, len(data["school1"])):
        class_id = 'class' + str(i)
        for student in data["school1"][class_id]:
            if data["school1"][class_id][student]["name"] == name and data["school1"][class_id][student]["surname"] == surname:
                student_id = student
                class_index = class_id
                info = data["school1"][class_id][student]

    return [student_id, class_index, info]


def show_class(data, class_index):
    class_id = 'class' + str(class_index)
    for student in data["school1"][class_id]:
        print(student)
        print(data["school1"][class_id][student])


data = import_data()

program_state = 0
while program_state == 0:
    print("Possible actions: ")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. Register Attendance")
    print("4. Find Student")
    print("5. Schow class ")
    print("6. Save changes ")
    program_state = int(input('Enter option ... '))

    if program_state == 1:
        print("Choose Class")
        print("Classes from 1 to {max}".format(max=len(data["school1"])))
        class_id = input("Enter only number ... ")
        name = input("Enter name of the student: ")
        surname = input("Enter surname of the student: ")
        add_student(data, class_id, name, surname)
        program_state = 0

    if program_state == 2:
        grade = int(input("Enter grade: "))
        class_index = int(input("Enter class: "))
        student_index = int(input("Enter student id: "))
        add_grade(data, class_index, student_index, grade)
        program_state = 0

    if program_state == 3:
        print("Enter 1 if present and 0 if not.")
        att = input("Enter attendance: ")
        class_index = int(input("Enter class: "))
        student_index = int(input("Enter student id: "))
        reg_att(data, class_index, student_index, att)
        program_state = 0

    if program_state == 4:
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        print(find_student(data, name, surname))
        program_state = 0

    if program_state == 5:
        class_index = input("Enter class: ")
        show_class(data, class_index)
        x = input("Press a key to continue.")
        program_state = 0

    if program_state == 6:
        save_data(data)
