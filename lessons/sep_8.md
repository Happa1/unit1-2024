# Sep 8
```.py

def frame_maker(msg:str, symbol:str, spaces:int)->str:
    height=5
    width=2+2*spaces+len(msg)
    red="\33[4;31m"
    end_code="\033[00m"

    top_line=symbol*width
    middle_line=symbol + " "*(width-2) + symbol
    msg_line=symbol + " "*spaces + msg.upper() + " "*spaces + symbol

    banner=f"{top_line}\n{middle_line}\n{red}{msg_line}{end_code}\n{middle_line}\n{top_line}"
    return banner

welcome=frame_maker(msg="welcome to Conbini", symbol="#", spaces=40)
print(welcome)
logo ="""
        _.-.
       ,'/ //)
      /// // /)
     /// // //|
    /// // ///
   /// // ///
  (`: // ///
   `;`: ///
   / /:`:/
  / /  `'
 / /
(_/  Combini
"""
print(logo)

#          Menu
with open("database.csv", 'r') as myfile:
    database = myfile.readlines()

items =[]
prices=[]
for line in database:
    # print(line)
    line=line.strip() #this removes the \n
    name, price = line.split(',')
    items.append(name)
    prices.append(int(price))

print(database)

#
# items=['onigiri', 'bread', 'chips']
# prices =[500, 200, 150]
#Menu
#1. Onigiri....................¥500
#2. bread......................¥200

print("Menu".center(50))
for it in range(len(items)):
    print(f"{it+1}. {items[it].title().ljust(50,'.')}¥{prices[it]}")

order = []
ordering=True
total=0
while ordering:
    selection = input(f"Please enter an item (1-{len(items)}):")
    available =""
    for i in range (len(items)):
        available += str(i+1) #availableの範囲をdefinesuru

    while not (selection.isdigit()and selection in available):
        selection = input(f"Please enter an item (1-{len(items)}):")#availableの範囲でない数字が入力されたときに実行試合
    #add up the prices to the total
    order.append(int(selection)-1)#input the number into list order
    total += prices[int(selection)-1]#total price of all items

    for it in range(len(items)):# allocate number to items (0-2)
        count = 0
        for o in order:#list order (0-2)
            if o==it:# order number == item number
                count +=1 #count +1
        if count>0: #print if you buy more than 1
            total_price = prices[it]*count #each item's total price is price list x the number you purchased
            print(f"{items[it].title().ljust(20)}x{count}=¥{total_price}")#Onigirix1=¥500

    answer = input("In this the last item?(Y/N)")
    while not answer in "yYnN":
        answer = input("Error. Last item(Y/N)")

    if answer in "yY":
        ordering = False

# print the total, plus tax (10%) inside the frame
print(frame_maker(msg=f"You pay ¥{(total*1.1):.2f}", spaces=50, symbol="$"))

with open("sales.csv", "a") as myfile: #option a:mean append
    myfile.writelines(f"order date total ¥{(total*1.1):.2f}\n")


```
