# QUESTION 1: Take an input string from the user and create a new string  with the first, middle, and last characters of
# the input string

# Get the inputted string as a variable
user_string = input("Input a string: ")
print(user_string)
# Get the first character using index 0
first_char = user_string[0]
# Get the last character using index -1
last_char = user_string[-1]

# For the middle character:

# Get the number of characters the string has using len()
str_length = len(user_string)
# Get the index of the middle character - len/2
mid_index = int(str_length/2)  # Since indices can only be integers
# Get the character at the middle index using str[mid_index]
mid_char = user_string[mid_index]
# Concatenate a, b, c together
result_string = first_char + mid_char + last_char
print(result_string)
