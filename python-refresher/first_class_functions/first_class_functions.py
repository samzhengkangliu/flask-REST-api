# First-class functions
def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"

def calculate(*values, operator):
    return operator(*values)

result = calculate(20, 4, operator=divide)
print(result)


def search(sequence, expected, finder):
    for element in sequence:
        if finder(element) == expected:
            return element
    raise RuntimeError(f"Could not find an element with {expected}.")

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, "Anne Pun", get_friend_name))