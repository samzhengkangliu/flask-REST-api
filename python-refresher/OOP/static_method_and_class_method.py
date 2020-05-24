# @classmethod @staticmethod
class ClassTest:
    # use for most things
    def instance_method(self):
        print(f"Called instance_method of {self}")

    # This can be called without creating an instance
    # Often use with factories
    @classmethod
    def class_method(cls):
        print(f"Called class_method with {cls}")

    # This can be called without creating an instance and also without the class
    # Used for place methods within a class
    @staticmethod
    def static_method():
        print("Called static_method.")


ClassTest.class_method()
ClassTest.static_method()

# Class Factory example
class Book:
    # attributes
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)

book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 500)

print(book)
print(light)

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return cls(store.name + " - franchise")

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return "{}, total stock price: {}".format(store.name, store.stock_price())