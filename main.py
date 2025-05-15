# Task 1 - Working with Lists
fruits = ["apple", "orange", "pineapple", "lemon", "cherry"]
print("Original list: ", fruits)

fruits.append("strawberry")
print("After adding a fruit: ", fruits)

fruits.remove("lemon")
print("After removing a fruit: ", fruits)

print("Reversed list: ", fruits[::-1])

# Task 2 - Exploring Dictionaries
person = {
    "name": "Lawrence",
    "age": 20,
    "city": "Murphy"
}

person.update({"favorite color": "black"})
person.update(city="Richardson")

print("\nKeys: ", end = "")
for key in person:
    print(key, end = ", ")

print("\nValues: ", end = "")
for key in person:
    print(person[key], end = ", ")

# Task 3 - Using Tuples
tup = ("The Matrix", "Mr. Fixer", "Book")
print("\n\nFavorite Things:", tup)

# tup[1] = "Song"
print("Oops! Tuples cannot be changed.")

print("Length of tuple:", len(tup))
