def add(x, y):
    return x + y

# Lambda version: Normally we don't give it a name
# if need a name just name it like: add = lambda
lambda x, y: x + y

def double(x):
    return x*2

sequence = [1, 3, 5, 7]

# lambda version
doubled = [(lambda x: x * 2)(x) for x in sequence]

doubled = list(map(lambda x: x * 2, sequence))

# List comprehension version
doubled = [double(x) for x in sequence]
# map 
doubled = map(double, sequence)