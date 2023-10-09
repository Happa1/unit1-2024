# Quiz014

Fig. 1 prompt of quiz 014

## 1.flow of chart

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

Fig. 3 test of quiz 014
