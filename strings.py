# Adding a comment in the remote repo
"""
print("Hello World")
# For variable names, do not use reserved keywords.
# print(help('keywords'))

# Assign multiple variables with the same value simultaneously
a = b = c = 10  # works but not recommended
print(a, b, c)

# Expression vs Statement
x = 47  # statement
y = 47 + 10  # expression

# TYPE CONVERSION #
# Convert to int
print(int(10.24))
print(int(float("10.24")))

# Convert to str
print(str(20))
print(type(str(20)))

# STRINGS #
# Can be created either by using single, double, or triple quotes
first_name = 'Jane'
print(first_name)

last_name = "Doe"
print(last_name)

address = '''10 Main St'''
print(address)

job1 = "Physician's Assistant"

# STRING FUNCTIONS #
emp_name = "Jane Doe"
# len() --> returns the number of characters in a given string
print(len(emp_name))

# upper and lower --> these convert the string into the corresponding cases
print(emp_name.upper())

# String concatenation
first_name = "Jane"
last_name = "Doe"
print(first_name + " " + last_name)

age = 24
print(first_name + " " + last_name + ": " + str(age))

# String multiplication
print("Hello"*3)

# Can only add 2 strings and can only multiply a string with an int

# Accessing string characters
emp_name = "Jane Doe"
print(emp_name[3])
# print(emp_name[8])  # throws index out of bouns error because the last char is at index 7

print(emp_name.index("n"))
"""

# STRING SLICING #
emp_name = "Jane Doe"
print(emp_name[2:6])
print(emp_name[:4])
print(emp_name[2:])
print(emp_name[-4:-1])

# [Start Value : End Value : Step Value]
print(emp_name[1:6:2])

# Returns an int with the number of times the specified value appears in the string
print(emp_name.count('e'))

# Gives an int that is the index of the position of where the specified value starts
print(emp_name.find('Doe'))

# Replaces
emp_name = emp_name.replace("Jane", "John")

# Returns a boolean that states if the specified value appears in the string or not
print("oh" in emp_name)

# String Formatting
student_name = "Alice"
score = 87
print(student_name + ": " + str(score))
print("Name: {} Score: {}".format(student_name, score))

# f-strings
print(f'Name: {student_name} Score: {score}')
print(f"10 times 3 is {10*3}")

