"""
An object representing a CLASS that describes the behavior of enrollStudent and validate the rule of a maximum of 10 students in a class
"""


class Course:
    def __init__(self):
        self.students = []

    def enroll_student(self, student):
        if len(self.students) < 10:
            self.students.append(student)
            return True
        else:
            return False

    def validate_rule(self):
        return len(self.students) <= 10
