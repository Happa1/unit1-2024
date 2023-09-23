# Quiz009
![Uploading Screen Shot 2023-09-23 at 13.42.44.png…]()

Fig. 1 prompt of quiz 009

## 1.flow of chart
<img width="868" alt="Screen Shot 2023-09-23 at 13 40 35" src="https://github.com/Happa1/unit1-2024/assets/142579414/69e4ed44-e34b-46dc-9d0a-b776fd3ca945">

Fig. 2 algorithm flow chart of quiz 009

## 2a.solution SL
```.py
# quiz 009 SL
def powersTen(num:int) -> str:
    units=['Tera', 'Giga', 'Mega','kilo','unit','mili','micro','nano','pico']
    power=[12,9,6,3,0,0,1,2,3]
    output=''
    count_0=''

    for n in range(len(units)):
        if n <4:
            count_0='0'*power[n]
            reversed_str = str(count_0)[::-1]
            separated_str = ' '.join(reversed_str[i:i + 3] for i in range(0, len(reversed_str), 3))
            output+=f"{num} {separated_str[::-1]}{units[n].rjust(30+n*4,' ')}\n"
            # power -= 3

        elif n==4:
            output +=f"{num}{units[n].rjust(30+n*4,' ')}\n"

        else:
            output += f"0.{'000 ' * (power[n])}00{num}{units[n].rjust(34-(n-7)*4,' ')}\n"

    return output

out=powersTen(1)
print(out)
```

## 2b.solution HL
```.py
# quiz 009 HL
import re
def powersTen(input:str) -> str:
    num = re.sub(r"\D", "", input)
    input_unit = re.sub(r"[^a-zA-Z]", " ", input)
    units=['Tera', 'Giga', 'Mega','kilo','unit','mili','micro','nano','pico']
    power=[12,9,6,3,0,0,1,2,3]
    output=''
    count_0=''

    for n in range(len(units)):
        if n <4:
            count_0='0'*power[n]
            reversed_str = str(count_0)[::-1]
            separated_str = ' '.join(reversed_str[i:i + 3] for i in range(0, len(reversed_str), 3))
            output+=f"{num} {separated_str[::-1]}{input_unit}{units[n].rjust(30+n*4,' ')}\n"
            # power -= 3

        elif n==4:
            output +=f"{num}{input_unit}{units[n].rjust(30+n*4,' ')}\n"

        else:
            output += f"0.{'000 ' * (power[n])}00{num}{input_unit}{units[n].rjust(34-(n-7)*4,' ')}\n"

    return output

input=(input("please enter a strings with units"))
out=powersTen(input)
print(out)
```

## 3.proof of work
<img width="528" alt="Screen Shot 2023-09-23 at 13 41 21" src="https://github.com/Happa1/unit1-2024/assets/142579414/879e4708-4659-4185-86d2-cb5f4ae23109">
Fig. 3 test of quiz 009 SL 

<img width="623" alt="Screen Shot 2023-09-23 at 13 41 53" src="https://github.com/Happa1/unit1-2024/assets/142579414/2e6b1600-6d53-42b0-9e42-f610fb1d1ab5">

Fig. 4 test of quiz 009 HL
