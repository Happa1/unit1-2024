# Quiz 003
![2023  Quizzes (2)](https://github.com/Happa1/unit1-2024/assets/142579414/c53b30e3-4887-4455-aaf3-53cb576904e6)

# 1.flow diagram
![Computer Science quiz (2)](https://github.com/Happa1/unit1-2024/assets/142579414/8adbc6bc-2ef2-4399-9731-161876b6b3dc)



# 2.solution
```.py
# quiz 003
in_protein=str(input("please input alphabet"))
def DNAtranslator(in_protein: str):
    out_protein = ''
    if in_protein=='A':
        out_protein='T'
    elif in_protein=='G':
        out_protein='C'
    elif in_protein=='T':
        out_protein='A'
    elif in_protein=='C':
        out_protein='G'
    else:
        print("invalid")
    return out_protein

out_protein=DNAtranslator(in_protein)
print(out_protein)

# quiz003 HL
in_protein=str(input("please input alphabet"))
def DNAtranslator(in_protein: str) ->str:
    out_protein = ''
    for char in in_protein:
        if char == 'A':
            out_protein += 'T'
        elif char == 'G':
            out_protein += 'C'
        elif char == 'T':
            out_protein += 'A'
        elif char == 'C':
            out_protein += 'G'
        else:
            print("invalid")

    return out_protein

test = DNAtranslator(in_protein)
print(test)
```
# 3.proof of work
<img width="329" alt="Screen Shot 2023-09-04 at 17 17 01" src="https://github.com/Happa1/unit1-2024/assets/142579414/baa4b492-0406-4e3d-8fb6-b4b4d6ed3e32">

