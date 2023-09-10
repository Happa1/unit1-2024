# Quiz 002
![2023  Quizzes (1)](https://github.com/Happa1/unit1-2024/assets/142579414/d2db10f6-a70e-4877-aa46-d512856f6fea)

# 1.flow diagram
![Computer Science quiz (1)](https://github.com/Happa1/unit1-2024/assets/142579414/f45fe4ec-41c9-4ccc-855b-d04e14c0f5b2)

# 2.solution
```,py
A = int(input("please enter number A"))
B = int(input("please enter number B"))

if A==20 or B ==20:
    print("True")
else:
    if A+B == 20:
        print("True")
    else:
        print("False")

# quiz002 HL
A2 = [10, 30, 10, 26]
B2 = [20, 15, 5, -6]
output="False"
count=0

for i in range(len(A2)):
    if A2[count]==20 or B2[count]==20:
        output='True'
    elif A2[count]+B2[count]==20:
        output = 'True'
    count+=1
print(output)
```

# 3.proof of work
<img width="299" alt="Screen Shot 2023-09-04 at 17 13 55" src="https://github.com/Happa1/unit1-2024/assets/142579414/69f545a2-5a96-4be8-8426-3d6ef055627b">
