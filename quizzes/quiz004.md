# Quiz 004
![2023  Quizzes (3)](https://github.com/Happa1/unit1-2024/assets/142579414/03077e05-72a5-4f1e-8e81-686ab6632b65)

# 1.flow diagram
![Computer Science quiz (3)](https://github.com/Happa1/unit1-2024/assets/142579414/ffb7d04c-7c34-4742-95da-f3339931ec62)


# 2.solution
```.py
#quiz 004
input_number = int(input("please enter a number"))

for i in range(1, input_number):
    if (input_number)%i==0:
        print(i)

#quiz004 HL
input_number = int(input("please enter a number"))
output=0
for i in range(1, input_number):
    if (input_number)%i==0:
        print(i)
        output += i
if input_number==output:
    print('True')
else:
    print('False')
```

# 3.proof my work
<img width="406" alt="Screen Shot 2023-09-05 at 7 00 52" src="https://github.com/Happa1/unit1-2024/assets/142579414/2998f951-6f94-47ef-b30e-f8b4212023e0">

