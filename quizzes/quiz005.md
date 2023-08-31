# Quiz005

# 1. flow diagram

# 2.solution

```.py

def sum_letters(text: str) -> int:
    alphabet = "abcdefghijklmnopqrstuvwxyz" # alphabet という関数にアルファベット26文字が入る
    sum_total = 0

    for let in text.lower():
        index =-1 # index start from -1
        for i in range (len(alphabet)):
            if let == alphabet[i]:
                index = i+1
                sum_total += index
    return sum_total

#proof of work
case1 = sum_letters(text="Math")
print(case1)

```

# 3. proof of work

