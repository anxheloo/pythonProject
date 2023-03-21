#If Statements

isMale = False
isTall = True

if isMale and isTall:
    print("You are a tall male")               #True / True
elif isMale and not(isTall):
    print("You are a short Male")              #True / False
elif not(isMale) and isTall:
    print("You are not a Male but are tall")   #False / True
else:
    print("You are not a male and not tall")   #both false


#If Statements and Comparisons

def max_num(num1,num2,num3):          #find the maximum number using this function
    if num1>num2 and num1>num3:
     return num1
    elif num2>num1 and num2>num3:
     return num2
    else:
        return num3



print(max_num(4,4,4))