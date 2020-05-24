# _str_ and _repr_
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Magic method for turning object to string
    def __str__(self):
        return self.name
    
    # Magic method for print out an umbigious representation of an object
    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"


bob = Person("Bob", 25)
print(bob)