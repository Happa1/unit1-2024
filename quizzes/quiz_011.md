# Quiz011
<img width="973" alt="Screen Shot 2023-09-23 at 12 54 18" src="https://github.com/Happa1/unit1-2024/assets/142579414/9b60d323-5daf-414a-8187-27a5426e05f8">

Fig. 1 prompt of quiz 011

## 1.flow of chart
<img width="343" alt="Screen Shot 2023-09-19 at 19 38 54" src="https://github.com/Happa1/unit1-2024/assets/142579414/dfee53f8-437f-4065-9f26-dc7fb1bc5347">

Fig. 2 algorithm flow chart of quiz 011

## 2.solution
```.py
def mulTable (input:int) -> str:
    output=0
    output_str=''
    if 2<=input<=10:
        for i in range (1,10):
            output=input*i
            output_str+=f"{input} x {i} = {output:2d}\n"

        return output_str

out=mulTable(2)
print(out)
```

## 3.proof of work
<img width="449" alt="Screen Shot 2023-09-19 at 19 39 21" src="https://github.com/Happa1/unit1-2024/assets/142579414/33228eb7-ba29-4c5f-890b-23a9bd1882e7">

Fig. 3 test of quiz 011
