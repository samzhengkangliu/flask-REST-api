def say_hello(name, surname):
    print(f"Hello, {name} {surname}")

# default position arguments
say_hello("Sam", "Liu")
# Use keyword arguments
say_hello(surname="Liu", name="Sam")

# Default parameter (must go at the end or after the non-default parameter)
def add(x, y=8):
    print(x + y)

add(1)
