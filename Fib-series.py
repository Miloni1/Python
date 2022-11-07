# [0,1,1,2,3,5,8,13....]

def fib(n): 
    #if n < 1:
         #return None
    #if n < 3:
        #return 1
    c = 0
    a = 0
    b = 1
    while n > 0:
    #for a in range(2,n+1):# i =2 sum = 2+1 = 3  i 
        c = a+ b
        #print(c)# sum = 3
        a, b = b,c # a=1,b=2, a=2 b=3
        n = n-1
    return c    
    
list = [0,1]
for n in range(1,10):
    list.append(fib(n))
print(list)

    