# Quiz015
![2023  Quizzes (5)](https://github.com/Happa1/unit1-2024/assets/142579414/89b3d2b5-3dbd-4878-998a-c81a67bfd27b)

Fig. 1 prompt of quiz 015

## 1.flow of chart
![Computer Science quiz (6)](https://github.com/Happa1/unit1-2024/assets/142579414/2bc230a9-9ded-431c-84bc-de996bbbdafc)

Fig. 2 algorithm flow chart of quiz 015

## 2.solution
### 2a. solution SL
```.py
def open_doors(num_students:int)->int:
    count_every = 1
    door=[0]*5#open=1, close=0
    for n in range(5):
        for i in range(5):
            if (i+1) % count_every==0:
                if door[i]==0:
                    door[i]=1
                else:
                    door[i] =0
        count_every += 1
    output=door.count(1)
    return output
out=open_doors(num_students=5)
print(out)
```

### 2b. solution HL
```.py
def open_doors(num_students:int)->int:
    count_every = 1
    door=[0]*num_students
    for n in range(num_students):
        for i in range(num_students):
            if (i+1) % count_every==0:
                if door[i]==0:
                    door[i]=1
                else:
                    door[i] =0
        count_every += 1
    output=door.count(1)
    return output

out=open_doors(num_students=10)
print(out)
```

## 3.proof of work
### 3a. proof SL
<img width="512" alt="Screenshot 2023-10-09 at 21 16 05" src="https://github.com/Happa1/unit1-2024/assets/142579414/e2ff0bf9-281d-4c0d-b836-3247cee03b82">
Fig. 3 test of quiz 015 SL

### 3b. proof HL
<img width="470" alt="Screenshot 2023-10-09 at 21 16 42" src="https://github.com/Happa1/unit1-2024/assets/142579414/4d342356-32b0-46e2-bc2f-e70c0ec29c37">

Fig. 4 test of quiz 015 Hl
