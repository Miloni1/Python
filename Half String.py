#first half string
string1 = input("Enter any name:")
string2 = ""
x = (len(string1))//2
for i in range(1,len(string1)-1):
    string2+=string1[i]
print(string2)    
        