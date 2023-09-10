# Quiz1
 ![2023  Quizzes](https://github.com/Happa1/unit1-2024/assets/142579414/7df5536d-f3d8-4b37-8fa1-b4ca9f3b15ee)


# 1.flow diagram
![Computer Science quiz](https://github.com/Happa1/unit1-2024/assets/142579414/521ae213-f788-4672-995e-ce228d1ce966)

# 2.solution
```.py
input = str(input("please enter"))
input_split=input.split()

output = 0
for index in input_split:
    str_count = len(index)
    # print(str_count)
    if str_count>2:
        for i in range(1,str_count-1):
            output+=1
        str_output = str(output)
        print(index[0] + str_output + index[-1],end=" ")
        output=0

    else:
        print(index, end=" ")
```
# 3.proof of work
<img width="442" alt="Screen Shot 2023-09-02 at 10 47 59" src="https://github.com/Happa1/unit1-2024/assets/142579414/9042b57e-457a-49fa-b864-be362ad26b5f">
