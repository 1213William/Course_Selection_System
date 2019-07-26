class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.course = []
        self.teacher = []
        self.student = []

    def add_to_course(self, course):
        self.course.append(course)

    def add_to_teacher(self, teacher):
        self.teacher.append(teacher)

    def add_to_student(self, student):
        self.student.append(student)


class Teacher:
    def __init__(self, name):
        self.name = name
        self.course = []
        self.school = []

    def add_to_course(self, course):
        self.course.append(course)

    def add_to_school(self, school):
        self.school.append(school)


class Course:
    def __init__(self, name, cycle, money):
        self.name = name
        self.cycle = cycle
        self.money = money
        self.student = []

    def add_to_student(self, student):
        self.student.append(student)


class Student:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.course = []
        self.score = None

    def add_to_course(self, course):
        self.course.append(course)

    def add_to_score(self, score):
        self.score = score


