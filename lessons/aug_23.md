# intro.py
# Today we will work on easy programming
"""
Today we will use input and output functinos
aug23
"""

my_name = "Manaha Ueda" # this is a string
my_email = '2025.manaha.ueda@uwcisak.jp'
is_student = True #this is a boolean True:1 or False:0
my_age = 16 # this is an integer
my_height = 154.5 # this is a float

# Show messages with
print(my_name)
print(my_email, my_age, end="")
print(my_height)

#f-string
print
print("Welcome", my_name, "your name is", my_email)
print(f"Welcome {my_name}, your email is {my_email}")


"""position = input("Please enter your position") # input only receieve string
salary = int( input("Please enter your salary JPY"))

print(f"Your position is {position} and salary is {salary}")
"""


"""first_name=input("Please enter your first name")
last_name=input("Please enter your last name")
year=int(input("Please enter your year"))

print(type(year))

print(f"{year}.{first_name}.{last_name}@uwcisak.jp")"""

#validating correct inputs from users
"""while True:
    raw_year = input("Enter your year")
    if raw_year.isdigit() ==True:
        year = int(raw_year)
        break

first_name=input("Please enter your first name")
x = first_name.title()
last_name=input("Please enter your last name")
print(f"{year}.{x}.{last_name}@uwcisak.jp")"""


# use in and endwith() to vertify email address
"""
school_email= input("please input your email")
    while True:
    if "@" in school_email:
        if school_email.endswith("uwcisak.jp")==True:
            school_email2=school_email
            break

print(f"{school_email2} is it a uwcisak user")
"""

#use specific letters to vertify email
import re
pattern = "^[0-9]+\.[a-zA-Z0-9_.+-]+\.[a-zA-Z0-9_.+-]+@uwcisak+\.jp"

while True:
    school_email = input("Please input your email: ")
    if re.match(pattern, school_email):
        print(f"{school_email} is a valid uwcisak user")
        break
    else:
        print("Invalid email. Please enter a valid uwcisak.jp email.")
