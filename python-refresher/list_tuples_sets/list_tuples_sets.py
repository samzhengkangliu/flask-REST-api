# List Tuple and Set
# List: Add remove is allowed in list
l = ["Sam", "Roceley", "Java"]

# Tuple: You can not modify the tuple
t = ("Sam", "Roceley", "Java")
# Create a tuple with only single value
single = (15,)

# Set: Cannot have duplicate values and does not maintain exact order
# Therefore, subscript notation is not allowed
s = {"Sam", "Roceley", "Java"}

print(l[0])

l.append("Bob")
print(l)

l.remove("Bob")
print(l)

s.add("Bob")
print(s)