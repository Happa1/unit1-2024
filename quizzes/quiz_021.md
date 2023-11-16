# Quiz021
![2023  Quizzes (7)](https://github.com/Happa1/unit1-2024/assets/142579414/7742ba55-b8e7-40c9-a015-a04d7b9deef2)


Fig. 1 prompt of quiz 021

## 1.flow of chart
![Computer Science quiz (12)](https://github.com/Happa1/unit1-2024/assets/142579414/aedee7fe-36a5-4cfe-b86f-dc48386514c1)

Fig. 2 algorithm flow chart of quiz 021

## 2.solution
```.py
import  random

random.seed(1234)
def produce (n:int, m:int, s:int):
    x_out=[]
    y_out=[]
    for _ in range(n):
        x=random.randint(0,100)
        y=x**(0.5*((m/s)**2))
        x_out.append(x)
        y_out.append(y)

    return y_out,x_out

import matplotlib.pyplot as plt

plt.style.use('ggplot')

y,x=produce(n=5, m=3, s=2)

plt.plot(x, y, color='r', marker="*")
plt.xlabel("x", fontsize=20)
plt.ylabel("$y=x^{1/2*m/s}$", fontsize=20)
plt.show()
```

## 3.proof of work
<img width="639" alt="Screenshot 2023-11-16 at 20 58 45" src="https://github.com/Happa1/unit1-2024/assets/142579414/c4853da4-c7c2-4ba0-9d25-1ca90e9c346e">

Fig. 3 test of quiz 021

## truth table
![IMG_0175](https://github.com/Happa1/unit1-2024/assets/142579414/8189612d-0431-4d6f-b035-bbc16eb73cb9)

Fig. 4 truth table of quiz 021
