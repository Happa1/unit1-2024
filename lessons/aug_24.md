# Aug24.py

```.py
# Aug24.py

"""
integer checker1
"""
A = int(input("please enter a number"))

if A>0:
    print("the number is integer")
else:
    print("the number is not integer")

"""
integer checker2 original
"""
A = int(input("please enter a number"))
if isinstance(A, int):
    print("the number is integer")
else:
    print("the number is not integer")

"""
if statement excercise 1
"""
A = int(input("please enter A number"))
B = int(input("please enter B number"))
C = int(input("please enter C number"))

if A>B:
    if A>C:
        if B>C:
            print("A, B, C")
        else:
            print("A, C, B")
    else:
        print("C, A, B")
else:
    if A>C:
        print("B, A, C")
    else:
        if B>C:
            print("B, C, A")
        else:
            print("C, B, A")

"""
if statements exercise 2
"""
while True:
    try:
        salary = int(input("Please enter your salary"))
        tax = 0
        if salary>=0:
            if salary>=10001:
                if salary>=50001:
                    if salary>=100001:
                        tax =25
                    else:
                        tax = 15
                else:
                    tax = 10
            else:
                tax = 5
            output = salary + salary * tax / 100
            print(output)
            break
    except:
        print("please enter your salary again")

"""
if statements excecise 3
"""

name1 = input("please enter 1st person name")
name2 = input("please enter 2nd person name")
name3 = input("please enter 3rd person name")

if name1>name2:
    if name1>name3:
        if name2>name3:
            print(name3, name2, name1)
        else:
            print(name2, name3, name1)
    else:
        print(name2, name1, name3)
else:
    if name2>name3:
        if name1>name3:
            print(name3, name1, name2)
        else:
            print(name1, name2, name3)
    else:
        print(name3, name2, name1)

"""
if statements excercise 4
"""
while True:
    try:
        number_input = list(map(int, input("please enter either 4 or 5 numbers (enter space between numbers)").split()))
        number_count = len(number_input)
        if number_count == 4 or 5:
            number_sum=sum(number_input)
            if number_count == 4:
                median=(sorted(number_input)[1]+sorted(number_input)[2])/2
            else:
                median=sorted(number_input)[2]
            print(median)
        break
    except:
        print("please enter numbers again")

```


