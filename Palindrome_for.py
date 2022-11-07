#Check for a palindrome string civic, radar, level
def reverseas(str):
    restr = "" # 
    a = len(str) - 1
    while a>=0:
        restr = restr + (str[a])   #in    str = miloni
        a = a-1
    return restr

#print(reverseas("Python"))
word = str(input("Enter any name of your choice  : "))
if word == reverseas(word):
    print(word,"is Palindrome")
else:
    print(word, "is not Palindrome")


#for x in word:
 #   reverse = word[::-1]
  #  if word == reverse:
   #     print(word,"is Palindrome")
    #else:
     #   print(word, "is not Palindrome")
      #  break
   