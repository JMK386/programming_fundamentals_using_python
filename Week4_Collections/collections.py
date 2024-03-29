"""
# Lists
# 1. Allow us to hold duplicate values
# 2. Order is maintained
# 3. Can hold heterogeneous data

list1 = [10, "test", True, 20.24, 10]
print(list1)

# lent() --> returns the number of elements in a list
print(len(list1))

# index and slice
print(list1[2])  # accessing the element at the 3rd position
print(list1[1:4])
print(list1[-2])

# Lists can hold other lists too
list2 = [10, "hi", False, 22.12, ["Hello", True]]
print(list2)

# Creating an empty list
countries = []

# Elements can be added to a list using either append, insert, or extend
countries.append("USA")
countries.append("Canada")
countries.append("Mexico")
print(countries)  # append always adds elements at the end

countries.insert(1, "France")
print(countries)

countries2 = ["Germany", "Ukraine", "Italy"]
countries.extend(countries2)
print(countries)

countries.append(countries2)
print(countries)

# Remove an element - can use either remove or pop
countries.remove("France")
print(countries)

removed_country = countries.pop()
print(removed_country)
print(countries)

print(countries.pop(2))  # pop by default removes the last element, but we can also specify a particular index

# Sorting lists
countries.sort()  # in-place functions modify the internal contents of the list
print(countries)

num_list = [1, 2, 3, 4, 5]
num_list.sort(reverse=True)
print(num_list)

# Membership Test
print("USA" in countries)

# Creating a string from list elements
countries_str = "-".join(countries)
print(countries_str)
print(type(countries))
print(type(countries_str))

# Creating a list by breaking a string into different elements
countries3 = countries_str.split("-")
print(countries3)


# TUPLES
# similar to lists, but once they are created, we cannot add or remove any elements from it
tuple1 = (36, 45, 32, 45, 3468)
print(tuple1)  # order maintained and duplicates allowed
print(tuple1[2])

# tuple1[2] = 89  cannot modify, add, or remove
# Can access or slice a tuple

# SETS
# 1. Do not allow duplicate values
# 2. Order is not guaranteed

courses = {"Networking", "English", "Math", "English", "History"}
print(courses)
print("Math" in courses)

# Widely used for 'set' operations
courses1 = {"Networking", "Physics", "Programming"}
print(courses.intersection(courses1))
print(courses.union(courses1))

print(courses.difference(courses1))
print(courses1.difference(courses))

courses.add("Psychology")
courses.remove("Math")
print(courses)

# DICTIONARIES
# stores key-value pairs
employees = {
    "id": 2133,
    "name": "Jane Doe",
    "salary": 4500,
    "skills": ["Java", "SQL", "C#"],
    "address": {
        "city": "NYC",
        "state": "NY",
        "zip-code": 12213
    }
}

print(employees)
# accessing dictionary values
print(employees["name"])
print(employees["address"]["city"])

employees["name"] = "Ryan"
print(employees)

employees.update({"name": "Jane Watson", "salary": 5000})
print(employees)

# Deleting key
del employees["salary"]
print(employees)

# Accessing keys
print(employees.get("address"))
print(employees.get("phone"))  # .get doesn't sent an error
# print (employees("Phone:)) # gives an error
print(employees.get("phone", "Not Found!"))

# Creating Empty Collections
list1 = []
tuple1 = ()

# tuple with a single element
tuple2 = (10,)
# behaves as the type of whatever is inside
# use a comma to consider it as a tuple
print(type(tuple2))

# set1 = {}  # This will create a dictionary
set1 = set()
print(type(set1))
dict1 = {}
"""

# Accessing Collection Items
list1 = [34, 43, 65, 7, [45, 56, 20, [1234, 233, 6578]], 4]
print(list1[4][3][1])
list1[2] = 99  # Changing an index to a new value
list1.index(7)  # Returns the position of a given value in the list
# tuples also support indexing and slicing

set1 = {34, 235, 32, 1}
# print(set1[2]) won't work because sets don't maintain order

dict1 = {
    "name": "John",
    "age": 25,
    "address": {
        "city": "Boston",
        "state": "MA",
        "zip": 12434
    },
    "skills": ["java", "SQL", "PHP"]
}

print(dict1["address"]["state"])

employee_details = [
    {
        "name": "John",
        "age": 25,
        "address": {
            "city": "Boston",
            "state": "MA",
            "zip": 12434
        },
        "skills": ["java", "SQL", "PHP"]
    },
    {
        "name": "Alex",
        "age": 46,
        "address": {
            "city": "NYC",
            "state": "NY",
            "zip": 12434
        },
        "skills": ["java", "SQL", "PHP"]
    }
]

# List and Tuple to a Set
list2 = [343, 3, 5, 8, 10, 3]
set2 = set(list2)
print(set2)  # Does not return duplicates
