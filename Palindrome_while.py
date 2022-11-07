#Check for a palindrome string civic, radar, level
word = str(input("Enter any name of your choice  : "))
#x = 0
while True:
    reverse = word[::-1]
    if word == reverse:
        print(word,"is Palindrome")
    else:
        print(word, "is not Palindrome")
    break
    

    
