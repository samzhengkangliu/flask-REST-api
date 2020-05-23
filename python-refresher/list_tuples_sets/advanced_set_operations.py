friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}
local = {"Rolf"}

# To create an empty set -> set()
# Get the differences
local_friends = friends.difference(abroad)
print(local_friends)

# Unite two sets
all_friends = abroad.union(local)
print(all_friends)

# Find out intersection
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}
both = art.intersection(science)
print(both)
