# if-else
"""
height = int(input("Please enter your height in cms: "))

if height > 120:
    print("Can ride")
else:
    print("Can't ride")


# Nested if-else
height = int(input("Please enter your height in cms: "))

if height > 120:
    print("Can ride")
    age = int(input("Enter your age: "))
    if age > 18:
        print("Ticket is $12")
    else:
        print("Ticket is $7")
else:
    print("Can't ride")


# elif
height = int(input("Please enter your height in cms: "))
bill = 0

if height > 120:
    print("Can ride")
    age = int(input("Enter your age: "))
    if age < 12:
        ticket_price = 5
        print("Ticket price is $5")
    elif age >=12 and age < 18:
        ticket_price = 7
        print("Ticket price is $7")
    elif age >= 18 and age < 45:
        ticket_price = 12
        print("Ticket price is $12")
    else:
        ticket_price = 0
        print("Ticket price is $0")
    want_photos = input("Do you want a photo taken? Enter Y/y or N/n: ")

    if want_photos == "Y" or want_photos == "y":
        bill = ticket_price + 3
        print(f"Your final bill is ${bill}")
    else:
        print(f"Your final bill is ${ticket_price}")
else:
    print("Can't ride")


# Grade Calculator
grade = int(input("Input the your grade percentage without the % sign: "))

if grade < 60 :
    print("F")
elif grade < 70:
    if grade < 63:
        print("D-")
    elif 63 < grade < 67:
        print("D")
    else:
        print("D+")
elif grade < 80:
    if grade < 73:
        print("C-")
    elif 73 < grade < 77:
        print("C")
    else:
        print("C+")
elif grade < 90:
    if grade < 83:
        print("B-")
    elif 83 < grade < 87:
        print("B")
    else:
        print("B+")
elif grade < 100:
    if grade < 93:
        print("A-")
    elif 93 < grade < 97:
        print("A")
    else:
        print("A+")
"""

# Exercise
"""
Ask user to enter a digit between 0 and 9
Return the corresponding word
Ex: user enters 1 --> program returns 'One' 
"""

num = int(input("Enter a digit between 0 and 9: "))
num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
print(f"Your number as a string is {num_list[num]}")


























