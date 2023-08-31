# Aug_30
## for loop

```.py
"""quiz 004"""
input_number = int(input("please enter a number"))

for i in range(1, input_number):
    output=''
    if (input_number)%i==0:
        print(i)

"""for loop"""
my_info=[20, "bob", "bob.square@pants.com", "deepsea"]

print(f"Hi my name is {my_info[1]}, I am {my_info[0]} years old")
index=0
for item in my_info:
    print(f"item {index}: {item}")
    index = index +1

"""how many letters in the email"""
count_letters=0
for letter in my_info[2]:
    count_letters=count_letters+1
print(f"number of letters in the email is {count_letters}")


"""count how many vowels inside the email and percentage of the vowels"""
cnt_vowels = 0
for letter in my_info[2]:
    if letter in 'aiueo':
        cnt_vowels += 1

print(f"number of bowel letters in the email is {cnt_vowels} this is {cnt_vowels/count_letters*100}%")

"""print all the numbers from 1: 2023"""
number = 0
for i in range(1, 2024): #range(start, end, step)
    print(f"year{number} i ={i}") #number is start from 1 and end with 2021, i is start from 1 and end with 2022
    number += 1

"""print all odd numbers from 0 to 1000"""
number = 0
for year in range(1, 1000, 2): #range(start, end, step)
    print(f"year{year}")
    number += 1

"""print 012 100times"""
for i in range(100):
    print(i%3)

"""print 100 memes"""
meme =['lol', 'omg', 'afp']
for i in range(100):
    # meme3=i%3
    print(meme[i%3], end='-') #use end to connect one line

```
