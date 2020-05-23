# Unpacking Arguments
# * means to do operations with each arguments
def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total

print(multiply(1, 3, 5))

print(multiply(-1))

def add(x, y):
    return x + y

nums = [3, 5]
print(add(*nums))

nums = {"x": 15, "y": 25}
# ** will pass in each key as the name argument  
print(add(**nums))


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else: 
        return "No valid operator provided to apply()."

print(apply(1, 3, 6, 7, operator="*"))