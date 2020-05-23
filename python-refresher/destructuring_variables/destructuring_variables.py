# Destructuring variables

# Tuples: 5, 11 (brackets are optional in this case)
x, y = 5, 11 

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

# return a list of tuples
print(list(student_attendance.items()))

# for student in student_attendance:
#     print(f"{student}: {student_attendance[student]}")

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

person=("Bob", 42, "Mechanic")
# ignore age here
name, _, profession = person
print(name, profession)

# split into two lists with head and the rest
head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)




