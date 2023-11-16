# Quiz017
[[2023] Quizzes.pdf](https://github.com/Happa1/unit1-2024/files/13376751/2023.Quizzes.pdf)

Fig. 1 prompt of quiz 017

## 1.flow of chart
![Computer Science quiz (7)](https://github.com/Happa1/unit1-2024/assets/142579414/3f4c96cf-b795-4ee5-b33c-39f6c7188d1a)

Fig. 2 algorithm flow chart of quiz 017

## 2.solution
### 2a solution SL
```.py
def get_l3tt3r (msg:str)->str:
    output=""
    for i in msg:
        if i=="a":
            output+="4"
        elif i=="e":
            output+="3"
        elif i=="i":
            output+="1"
        elif i=="o":
            output+="0"
        elif i==" ":
            output+="_"
        else:
            output+=i

    return output

case1=get_l3tt3r(msg="Hello World")
print(case1)
```

### 2a solution HL
```.py
def get_l3tt3r (msg:str)->str:
    letter = {"a":"4", "e":"3","i":"1","o":"0"," ":"_"}
    output = ""
    for i in msg:
       output += letter.get(i, i)
    return output

case1=get_l3tt3r(msg="Hello World")
print(case1)
```

## 3.proof of work
<img width="274" alt="Screenshot 2023-11-16 at 20 06 40" src="https://github.com/Happa1/unit1-2024/assets/142579414/ceed42e6-530d-4f09-86a4-ea6f0dbad7af">

Fig. 3 test of quiz 017

## Boolean circuit
![IMG_0171](https://github.com/Happa1/unit1-2024/assets/142579414/37f9aa35-2bcb-45b5-85d8-760279d34664)

