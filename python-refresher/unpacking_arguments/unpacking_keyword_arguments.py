# Unpacking Keyword Arguments
# ** will collect key word arguments and put into a dictionary
# OR unpack the keyword in dictionary arguments
def named(**kwargs):
    print(kwargs)


named(name="Bob", age=25)


def name(name, age):
    print(name, age)


details = {"name": "Bob", "age": 25}

name(**details)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg} : {value}")


print_nicely(name="Bob", age=25)


def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, name="Bob", age=25)
