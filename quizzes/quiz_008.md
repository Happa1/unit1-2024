# Quiz 008
# 1.flowchart
![Computer Science quiz (7)](https://github.com/Happa1/unit1-2024/assets/142579414/a425a1ac-0307-462c-a00c-c46e7d71cc46)

# 2.solution
```.py
# quiz008
input_text=input("please enter strings")
output=""
for ch in input_text:
    if ch in 'abcdefghijklmnopqrstuvwxyz':
    # if ch !=chr(32):
        an = ord(ch)+13
        if an >122:
            output+=chr(an-26)
        else:
            output+=chr(an)
    else:
        output+=" "
print(output)


# quiz008 HL
shift=int(input("please enter the number of shift(1-26)"))
while shift>27:
    shift = int(input("please enter the number of shift"))
input=input("please enter strings")
output=""
for ch in input:
    if ch in 'abcdefghijklmnopqrstuvwxyz':
    # if ch !=chr(32):
        an = ord(ch)+shift
        if an >122:
            output+=chr(an-26)
        else:
            output+=chr(an)
    else:
        output+=" "
print(output)
```
# 3.proof of work
<img width="472" alt="Screen Shot 2023-09-10 at 17 08 29" src="https://github.com/Happa1/unit1-2024/assets/142579414/9fbca073-f7a8-4e6c-9a19-79d9e59fe255">

