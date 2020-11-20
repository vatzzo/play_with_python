import json
import statistics
import random
from faker import Faker
faker = Faker()


class Student:
    def __init__(self, name, surname, grades=[], attendance=[]):
        self.name = name
        self.surname = surname
        self.grades = grades
        self.attendance = attendance
        self.avg = self.__calculate_avg()
        self.att_pr = self.__calculate_att_pr()

    def __calculate_avg(self):
        return statistics.mean(self.grades)

    def __calculate_att_pr(self):
        sum_total = 0
        for i in self.attendance:
            if i == 1:
                sum_total = sum_total + 1
        return sum_total/len(self.attendance)

    def add_grade(
        self, grade
    ):
        self.grades.append(grade)
        self.avg = self.__calculate_avg()

    def register_att(
        self, att
    ):
        self.attendance.append(att)
        self.att_pr = self.__calculate_att_pr()


class SchoolGrade:
    def __init__(self):
        self.students = []

    def add_student(
        self, student
    ):
        self.students.append(student)


class School:
    def __init__(self):
        self.classes = []

    def add_class(
        self, school_grade
    ):
        self.classes.append(school_grade)


def create_arr(length, min, max):
    tab = []
    for i in range(0, length-1):
        tab.append(random.randint(min, max))
    return tab


def convert_to_dict(obj):
    data = {}
    for i in range(0, len(obj)):
        data['school'+str(i+1)] = schools[i].__dict__
        for j in range(0, len(obj[i].classes)):
            data['school'+str(i+1)]['class'+str(j+1)
                                    ] = schools[i].classes[j].__dict__
            for k in range(0, len(obj[i].classes[j].students)):
                data['school'+str(i+1)]['class'+str(j+1)
                                        ]['student'+str(k+1)] = schools[i].classes[j].students[k].__dict__

    for i in range(0, len(obj)):
        for j in range(0, len(obj[i].classes)):
            data['school'+str(i+1)]['class'+str(j+1)].pop("students")
    data['school'+str(i+1)].pop("classes")

    return data


def save(data):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":
    number_of_students = input('Enter total number of students: ')
    number_of_classes = input('Enter total number of classes: ')
    number_of_schools = 1
    print('Generating data ...')

    students = []
    classes = []
    schools = []
    data = {}

    for i in range(0, int(number_of_schools)):
        schools.append(School())

    for i in range(0, int(number_of_classes)):
        classes.append(SchoolGrade())

    for i in range(0, int(number_of_students)):
        students.append(Student(str(faker.first_name()), str(
            faker.last_name()), create_arr(5, 1, 5), create_arr(5, 0, 1)))

    for i in students:
        j = random.randint(0, len(classes)-1)
        classes[j].add_student(i)

    for i in classes:
        j = random.randint(0, len(schools)-1)
        schools[j].add_class(i)

    data = convert_to_dict(schools)
    save(data)
