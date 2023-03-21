#Recursion is a Function that calls itself

#Factorial of 3 is 6: 3*2*1 . We will use Recursion to find the factorial of a number

#Way 1
def factoriall(x):
    if x == 1:
        return 1
    else:
        return x*(factoriall(x-1))


#Way 2
def factorialll(x):
    while x>0:
        return x * (factoriall(x - 1))
    x-=1


#Way 3 - selfmade
def factorial(x):
    result = 1
    while x>0:
        result = result * x
        x-=1

    return result


result = factorial(10)
result2 = factoriall(10)
result3 = factorialll(10)

print(result)
print(result2)
print(result3)