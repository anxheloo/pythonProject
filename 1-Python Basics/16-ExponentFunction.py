#Exponent Function

print(2**3)  #2 in power of 3

#way 1
def raiseToPower(baseNumber, powerNumber):
    result = 1

    for index in range(powerNumber):
        result = result * baseNumber

    return result


print(raiseToPower(2,4))


#way 2 base on java code on my laptop
def raiseToPower2(baseNumber, powerNumber):
    result = 1
    count = 1

    while count <= powerNumber:
        result = result * baseNumber
        count +=1
    return result



print(raiseToPower2(5,4))
