#use minimum coins to get the target value
import math
currency = [1,2,5,10,20,50,100]
target_value = 43
list = []
for i in currency:
    if target_value >= i:
        list.append(i)
print(list)
newlist = []
for i in list:
    newlist.insert(0,i)
print(newlist)
remaining_value = target_value
while remaining_value>0:
    coins = []
    for i in list:
        x = max(list)
        y = min(list)
        if remaining_value > x :
            remaining_value = remaining_value - x
            print(remaining_value)
            coins.append(x)
        else:
            remaining_value = remaining_value - y
            print(remaining_value,y)
            coins.append(y)
    print(coins)       
        
        
    

        
                
            
        



        
        
