#print first n factorials of a number
#Factorial number is a number that is multiplied by it's previous numbers. 

def factorial(n):
    fact = 1
    for x in range(1,n+1): # x in range of 1 - 6
        fact = fact * x # fact = 2*3 say x =3
    return fact


num = int(input("Enter any number: "))
ans = factorial(num)
print("Factorials of" ,num,"is", ans)
    
    

