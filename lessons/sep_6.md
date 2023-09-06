# Sep_6
```.py
# quiz006
count=0
for f in range(1,10+1):
    for r in range(1,10+1):
        count+=1
        print(f"{count}-Room{f}F{r:02d}")

# find 7 multiples
num=1
count=0
for i in range(1,10000+1):
      if i%7==0 and i%6==0:
        print(f"{num} is multiple of 6 and 7")
        count+=1
print(f"{num} is multiple of 6 and 7")

#find 500 6 and 7 multiples
num=1
count=0
while count<500:
    if num%7==0 and num%6==0:
        print(f"{num} is multiple of 6 and 7")
        count+=1
    num+=1
            # print(f"{count} is multiple of 6 and 7")
print(f"we counted up tp {num} to find 500 multiples")

# msg=str(input("please enter strings"))
import random


def frame_maker(msg:str, symbol:str, spaces:int)->str:
    height=5
    width=2+2*spaces+len(msg)
    red="\33[4;31m"
    end_code="\033[00m"

    top_line=symbol*width
    middle_line=symbol + " "*(width-2) + symbol
    msg_line=symbol + " "*spaces + msg.upper() + " "*spaces + symbol

    banner=f"{top_line}\n{middle_line}\n{red}{msg_line}{end_code}\n{middle_line}\n{top_line}"
    return banner

title="A Cool Game"
cool_game=frame_maker(msg=title, symbol="#", spaces=40)
print (cool_game)

#The guessiong number game
#Pick a random number 1-100
secret_number=random.randint(1,100)
#count how manny tries it took the user
count=0
#ask the user for a number, indicate if it is bigger or smaller than secreat number
guess=int(input("Please enter a guess (1-100): "))
while guess != secret_number:
    if guess > secret_number:
        print("Too big")
    else:
        print("Too small")

    guess=int(input("Please enter a guess (1-100): "))
    count+=1

print(f"you won, it took you {count} tries")

# msg=str(input("please enter strings"))
import random


def frame_maker(msg:str, symbol:str, spaces:int)->str:
    height=5
    width=2+2*spaces+len(msg)
    red="\33[4;31m"
    end_code="\033[00m"

    top_line=symbol*width
    middle_line=symbol + " "*(width-2) + symbol
    msg_line=symbol + " "*spaces + msg.upper() + " "*spaces + symbol

    banner=f"{top_line}\n{middle_line}\n{red}{msg_line}{end_code}\n{middle_line}\n{top_line}"
    return banner

title="A Cool Game"
cool_game=frame_maker(msg=title, symbol="#", spaces=40)
print (cool_game)

#The guessiong number game
#Pick a random number 1-100
secret_number=random.randint(1,100)
#count how manny tries it took the user
count=0
#ask the user for a number, indicate if it is bigger or smaller than secreat number
guess=int(input("Please enter a guess (1-100): "))
while guess != secret_number:
    if guess > secret_number:
        print("Too big")
    else:
        print("Too small")

    guess=int(input("Please enter a guess (1-100): "))
    count+=1

print(f"you won, it took you {count} tries")

# 2symbol + 2space+len(msg)


```
