#Get N numbers and print the sum of the given N numbers.
#Input 5        -> first number is the value of N followed by N numbers 12 34 20 40 25 Output 131 
#number = int(input("Enter any number:"))
times = int(input("Enter how many times number should be asked:"))
total = 0
while times!=0:
    number = int(input("Enter any number:"))
    total = total + number
    times = times-1
    
#print(number)
print (total)
            