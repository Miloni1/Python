#kth largest element of the list
list = [1,23,21,34,56,78,89]
newlist = []
k = int(input("Enter any position:"))
while k > 0:
    max = list[0]
    for i in list:
        if i not in newlist:
            if i> max :
                max = i
    newlist.append(max)    
    k = k-1       
     
print(newlist[k-1])
