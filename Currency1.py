#Minimum number of coins
import math
currency = [1,2,5,10,20,50,100]
target_value = int(input("Enter number: "))
newlist = []# create reverse list
for i in currency:
    newlist.insert(0,i)
#print (newlist)
count = 0 # number of coins used
coins = [] # list for coins
remaining_value = target_value
for i in newlist:
    while remaining_value>=i:
        #if remaining_value>i:
        remaining_value = remaining_value-i
            #coins.append(remi)
        #print(remaining_value,i)
        coins.append(i)
        count = count + 1
print(coins)
print("Minimum number of coins:",count)
            
    
            