# Quiz013
Create a function that receives one input and produces the output shown. 
out = mystery(A=37, B=3)
print(out)
| Input A:int , B:int | Output :int |
|---------------------|-------------|
| 37, 3               | 1372        |
| 58, 2               | 3366        |

※ We didn't have a slide of this prompt.


## 1.flow of chart
<img width="352" alt="Screen Shot 2023-09-20 at 9 30 57" src="https://github.com/Happa1/unit1-2024/assets/142579414/8afdb061-4767-4a40-b95f-dbab27f4d202">

Fig. 2 algorithm flow chart of quiz 013

## 2.solution
```.py
def mysteryTwo (A:int, B:int) -> int:
    return A**2+B

out=mysteryTwo(A=37, B=3)
print(out)
```

## 3.proof of work
<img width="650" alt="Screen Shot 2023-09-20 at 9 29 50" src="https://github.com/Happa1/unit1-2024/assets/142579414/18abbfeb-820b-4f6a-b5c8-82d921e5269f">
Fig. 3 test of quiz 013 with 1st given input

<img width="650" alt="Screen Shot 2023-09-20 at 9 30 30" src="https://github.com/Happa1/unit1-2024/assets/142579414/ca2621d0-0a16-473a-8ea1-f1782efef829">
Fig. 4 test of quiz 013 with 2nd given input
