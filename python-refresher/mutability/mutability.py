# Most things in Python are mutable except for tuples, strings, integers, floats and booleans
from typing import List, Optional


class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        self.name = name
        self.grades = grades or []  # New list created if one isn't passed

    def take_exam(self, result):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)  # Now it's empty.