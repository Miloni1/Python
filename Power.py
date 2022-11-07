#WAP(Write a program) to input 2 numbers, a number and its power ex. 2 and 3. Calculate 2^3
def power2(x,y):
    z = 1
    while y >=1:# y = 4,3,2,1
        z = z*x # 1*2, 2*2, 4*2, 8*2
        y = y-1
    return z

a = int(input("Enter any number = "))
b = int(input("Enter you want power of ="))
ans = power2(a,b)
print(ans)
   

  # power function  
