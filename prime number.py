#WAP to input a number from the user and find whether it is prime
x = int(input("Enter any number = "))# 15
for i in range(2, x):#i in range of 2 - 15
    if (x % i) == 0: #15%2 = 1 
        print("oops",x, " is not a Prime number.")
        break
else:
    print("Hurray",x, " is  Prime number.")
            
            