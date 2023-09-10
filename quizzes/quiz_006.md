# Quiz 006
![2023  Quizzes (5)](https://github.com/Happa1/unit1-2024/assets/142579414/b50e9c90-1183-42ad-b9ba-dc4ac27d339e)

# 1.flowchart
![Computer Science quiz (5)](https://github.com/Happa1/unit1-2024/assets/142579414/5291ac4e-7cf0-4a59-8734-a387d66e73e4)


# 2.solution
```.py
# quiz006
count=0
for floor in range(1,10+1):
    for room in range(1,10+1):
        count+=1
        print(f"{count}-Room {floor}F{room:02d}")

# quiz006 HL
count = 0
input=int(input("please enter the number"))
for floor in range(1, 10 + 1):
    for room in range(1, 10 + 1):
        count += 1
        if input==count:
            print(f"Room {floor}F{room:02d}")

```

# 3.proof of work
<img width="383" alt="Screen Shot 2023-09-10 at 16 48 39" src="https://github.com/Happa1/unit1-2024/assets/142579414/b0dd3394-d1e5-428d-b57b-fbe107d696d8">
