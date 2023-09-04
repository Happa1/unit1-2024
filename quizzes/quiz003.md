# 1.flow diagram
![Untitled (3)](https://github.com/Happa1/unit1-2024/assets/142579414/5a90cadd-4a2c-4f8f-9930-b3c61f5b09d2)


# 2.solution
```.py
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

"""Quiz003 HL"""
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

