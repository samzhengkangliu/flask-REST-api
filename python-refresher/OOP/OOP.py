# OOP
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

# create an object of student
student = Student("Sam", (92, 90, 93, 78, 90))
print(student.name)

print(student.average_grade())