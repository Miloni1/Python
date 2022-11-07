def isPrime(num):
    for i in range(2,num):#
        if num%i == 0  : # num = 17 i = 2
           return False
    #else:
    return True
list_primenumbers = []
x = int(input("enter any number:"))
for a in range(2,x):
    if isPrime(a):
        list_primenumbers.append(a)
print(list_primenumbers)