# Quiz014
![2023  Quizzes (4)](https://github.com/Happa1/unit1-2024/assets/142579414/25d80a89-9db3-4a4d-b208-9c8bcb3de2ed)
Fig. 1 prompt of quiz 014

## 1.flow of chart
![Computer Science quiz (5)](https://github.com/Happa1/unit1-2024/assets/142579414/9c2c349c-bc6a-4b1e-8025-f7d7b6a6b286)
Fig. 2 algorithm flow chart of quiz 014

## 2.solution
```.py
def blackBoxThree(given:str)-> str:
    given_lower=given.lower()
    output=''
    number=1
    for i in given_lower:
        if i in "abcdefghijklmnopqrstuvwxyz":
            count=str(given_lower.count(i,0,number))
            output+=count
        else:
            output+=i
        number+=1
    return output

out=blackBoxThree("hello world")
print(out)
```

## 3.proof of work
<img width="530" alt="Screenshot 2023-10-09 at 21 09 47" src="https://github.com/Happa1/unit1-2024/assets/142579414/6070643b-e62c-4bd1-93e2-650b9542b627">
Fig. 3 test of quiz 014
