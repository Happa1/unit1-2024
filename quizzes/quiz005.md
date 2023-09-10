# Quiz005
![2023  Quizzes (4)](https://github.com/Happa1/unit1-2024/assets/142579414/9e95e53c-c46f-4430-a2b6-3321f7d86021)


# 1. flow diagram
![Computer Science quiz (4)](https://github.com/Happa1/unit1-2024/assets/142579414/bba4870b-7ce1-43cc-b7d1-557b469ffc88)


# 2.solution

```.py

def sum_letters(text: str) -> int:
    alphabet = "abcdefghijklmnopqrstuvwxyz" # alphabet という関数にアルファベット26文字が入る
    sum_total = 0

    for let in text.lower():
        index =-1 # index start from -1
        for i in range (len(alphabet)):
            if let == alphabet[i]:
                index = i+1
                sum_total += index
    return sum_total

#proof of work
case1 = sum_letters(text="Math")
print(case1)

```

# 3. proof of work
<img width="419" alt="Screen Shot 2023-09-10 at 16 42 35" src="https://github.com/Happa1/unit1-2024/assets/142579414/97f08ae0-849b-4c75-af3a-daa2fee9116b">


