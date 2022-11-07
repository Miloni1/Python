def isYearLeap(year):
    if year%4==0:
        print("Leap Year")
def daysInMonth(year, month):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month== 2:
        if isYearLeap(year):
            return 29
        else:
            return 28
    elif month in [4,6,9,11]:
        return 30
    else:
        return none
        
def dayOfYear(year, month, day):
    if daysInMonth(year, month):
        if day<= 31:
            print("Valid Year,Month and day")
        else:
            print("Valid Year and Month  but not the day")
    
print(dayOfYear(1900, 10,16))