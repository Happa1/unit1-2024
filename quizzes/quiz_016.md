# Quiz016
![2023  Quizzes (6)](https://github.com/Happa1/unit1-2024/assets/142579414/263e9832-d0ef-499b-a9e0-54a2892f98d6)

Fig. 1 prompt of quiz 016

## 1.flow of chart
<img width="661" alt="Screenshot 2023-10-09 at 21 18 38" src="https://github.com/Happa1/unit1-2024/assets/142579414/caab8662-8e3c-4697-a77e-dc6dca3141fd">

Fig. 2 algorithm flow chart of quiz 016

## 2.solution
### quiz 016 SL
```.py
# quiz 016 SL
def averafeLenght(words:list)->int:
    count=len(words)
    letter_len=0

    for i in range(count):
        letter_len+=len(words[i])

    average=letter_len/count
    return average

out=averafeLenght(words=["hello", "main"])
print(out)
```

### quiz 016 HL
```.py
def averafeLenght(words):
    count=len(words)
    letter_len=0

    for i in range(count):
        words[i]=words[i].replace(' ', '')
        letter_len+=len(words[i])

    average=letter_len/count
    return average

out=averafeLenght(words=["Computer Science", "Art"])
print(out)
```

## 3.proof of work
### quiz 016 SL
<img width="557" alt="Screenshot 2023-10-09 at 21 19 53" src="https://github.com/Happa1/unit1-2024/assets/142579414/159770b8-37a4-402f-9bdf-23e86367adfa">

Fig. 3 test of quiz 016 SL

### quiz 016 HL
<img width="598" alt="Screenshot 2023-10-09 at 21 20 30" src="https://github.com/Happa1/unit1-2024/assets/142579414/b081d8a2-3e48-4d52-9fe5-e48eaed8a1a0">

Fig. 4 test of quiz 016 HL
