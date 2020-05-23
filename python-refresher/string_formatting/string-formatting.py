# f-string in Python (version > 3.6)
name = "Sam"

print(f"Hello, {name}")

name = "Roceley"

print(f"Hello, {name}")

# template strings with .format()
new_name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format(new_name)
print(with_name)

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Sam", "Friday")
print(formatted)
