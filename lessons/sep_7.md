# Sep_7

```.py
def frame_maker(msg:str, symbol:str, spaces:int)->str:
    height=5
    width=2+2*spaces+len(msg)

    top_line=symbol*width
    middle_line=symbol + " "*(width-2) + symbol
    msg_line=symbol + " "*spaces + msg.upper() + " "*spaces + symbol

    banner=f"{top_line}\n{middle_line}\n{msg_line}\n{middle_line}\n{top_line}"
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

#Menu
items=['onigiri', 'bread', 'chips']
prices =[500, 200, 150]
#Menu
#1. Onigiri....................¥500
#2. bread......................¥200

print("Menu".center(50))
for it in range(len(items)):
    print(f"{it+1}. {items[it].title().ljust(50,'.')}¥{prices[it]}")

order = []
order_count=[]
ordering=True
total=0
while ordering:
    selection = input(f"Please enter an item (1-{len(items)}):")
    available =""
    for i in range (len(items)):
        available += str(i+1) #availableの範囲をdefinesuru

    while not (selection.isdigit()and selection in available):
        selection = input(f"Please enter an item (1-{len(items)}):")#availableの範囲でない数字が入力されたときに実行しない
    #add up the prices to the total
    order.append(int(selection)-1)#input the number into list order
    total += prices[int(selection)-1]#total price of all items

    for it in range(len(items)):# allocate number to items (0-2)
        count = 0
        for o in order:#list order (0-2)
            if o==it:# order number == item numberだった時にその部分だけcountが増える
                count +=1 #count +1
                # order_count[it]=count
                print(f"order{order}")
                print(f"order{count}")
        if count>0: #print if you buy more than 1
            total_price = prices[it]*count #each item's total price is price list x the number you purchased
            print(f"{items[it].title().ljust(20)}x{count}=¥{total_price}")#Onigirix1=¥500

    answer = input("In this the last item?(Y/N)")
    while not answer in "yYnNdD":
        answer = input("Error. Last item(Y/N)")

    if answer in "dD":
        delete_item = input("Enter the number assigned for goods that you want to delete.")
        while not (delete_item.isdigit() and delete_item in available):
            delete_item = input("Please check again and enter the correct number assigned for goods that you want to delete.")
        delete_item_it = int(delete_item) - 1
        item_count = order.count(delete_item_it)
        print(f"itemcount{item_count}")

        delete_number = int(input("How many of this item do you want to delete?"))
        while delete_number > item_count:
            delete_number = int(input("Error. Type the number of delete again"))

        delete=input("Do you actually want to delete item?(Y/N)")
        while not delete in "yYnNdD":
            answer = input("Error. DO you want to delete item?(Y/N)")
        if delete in "Yy":
            print(f'You delete {delete_number} of {items[delete_item_it]}')
            delete_count=0
            print(order)
            while not delete_count > delete_number:
                for i in order:
                    if i == delete_item_it:
                        order=order.remove(delete_item_it)
                        delete_count+=1
                        if delete_count==delete_number:
                            break

    if answer in "yY":
        ordering = False

# print the total, plus tax (10%) inside the frame
print(frame_maker(msg=f"You pay ¥{(total*1.1):.2f}", spaces=50, symbol="$"))


pay=int(input("please enter the monye customer paid"))
while not pay>=(total*1.1):
    pay=int(input("please enter the monye customer paid again"))

change=(pay-(total*1.1))
print(f"the change is ${(change):.2f}")

```
