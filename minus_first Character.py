
def combo(a,b):
    string1 = ""
    string2 = ""
    for x in range(1,len(a)):
        string1 += a[x]
    for y in range(1,len(b)):
        string2 += b[y]
    
    print(string1+string2)        
        
        

a = str(input("Enter any name:"))
b = input("Enter any name:")
combo(a,b)


        