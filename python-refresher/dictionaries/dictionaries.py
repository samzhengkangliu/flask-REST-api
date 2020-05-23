# Dictionaries
friend_ages = {"Sam": 25, "Java": 5, "Roceley": 18}

friends = [
    {"name": "Sam", "age": 25},
    {"name": "Roceley", "age": 18},
    {"name": "Java", "age": 5},
]
# print(friends[1]["name"])

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")    

attendance_values = student_attendance.values() # will return a list of values
print(attendance_values)
print(sum(attendance_values) / len(attendance_values))