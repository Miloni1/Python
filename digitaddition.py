number = int(input("Enter any number = "))
total = 0
z= number # z = 3456
x = 0
while z>0:# 3456 >0 = true, 345 >0, 34 >0
    x = z % 10 # x = 6 , 5 , 4
    z= int(z /10) # z = 345 , 34
    total = total + x
    print(x)
print(total)


