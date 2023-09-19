# Quiz012
![2023  Quizzes (1)](https://github.com/Happa1/unit1-2024/assets/142579414/c3e0aae3-55f4-47f1-8781-d10c8d40b779)

Fig. 1 prompt of quiz 010

## 1.flow of chart
<img width="430" alt="Screen Shot 2023-09-19 at 19 43 11" src="https://github.com/Happa1/unit1-2024/assets/142579414/d874f32c-f572-4fb5-b05b-6a0d67b5b0b8">

Fig. 2 algorithm flow chart of quiz 010

## 2a.solution SL
```.py
def bestMonth (month:int):
    days=["We","Th","Fr","Sa","Su","Mo","Tu"]
    month_name="Novermber 2023"
    # days_index=0
    calendar=''
    days_row=''
    for d in range(1,30+1):
        calendar+=f" {d:2d}"
        if d%7==0:
            calendar+="\n"
    for i in range(7):
        days_row+=f" {days[i]}"

    return f"{month_name.center(21, ' ')}\n{days_row}\n{calendar}"

out=bestMonth(11)
print(out)
```

## 2b.solution HL
```.py
# quiz 010 HL
def bestMonth (month:int):
    month_name=["January", "February", "March", "April", "May", "June", "july", "August", "September", "October", "Novermber", "December"]
    days=["Su","Mo","Tu","We","Th","Fr","Sa"]
    days_index=0
    days_list=''
    date_count=0
    days_in_month=0
    this_month_date=0
    calendar=''

    if month==2:
        this_month_date=28
    elif month<8 and month%2==1:
        this_month_date=31
    elif month>=8 and month%2==0:
        this_month_date=31
    else:
        this_month_date=30

    for m in range(1,month):
        if m == 2:
            days_in_month = 28
        elif m < 8 and m % 2 == 1:
            days_in_month = 31
        elif m >= 8 and m % 2 == 0:
            days_in_month = 31
        else:
            days_in_month = 30
        date_count+=days_in_month

    days_index=(date_count+1)%7-1
    for index in range(days_index,7):
        days_list+=f" {days[index]}"
            # if index==7:
    for index_before in range(0,days_index):
        days_list+=f" {days[index_before]}"

    for d in range(1, this_month_date+1):
        calendar += f" {d:2d}"
        if d%7==0:
            calendar+="\n"
    title=month_name[month-1]+" 2023"
    return f"{title.center(21,' ')} \n{days_list}\n{calendar}"

out=bestMonth(int(input("please enter the bestmonth")))
print(out)

```

## 3.proof of work
<img width="353" alt="Screen Shot 2023-09-19 at 19 44 03" src="https://github.com/Happa1/unit1-2024/assets/142579414/141b5d7d-b19f-48da-9eb6-7255ed4e2aed">

Fig. 4 test of quiz 010 SL
<img width="465" alt="Screen Shot 2023-09-19 at 19 44 46" src="https://github.com/Happa1/unit1-2024/assets/142579414/fcb23463-6cef-4595-a7f9-b739ecfd17d9">

Fig. 3 test of quiz 010 HL
