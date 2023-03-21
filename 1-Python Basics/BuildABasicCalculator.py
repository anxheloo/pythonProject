num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2

print(result)  #The problem with this simple calculator is that python takes the input as strings

#So we need to convert the string to numbers

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2) #this will convert to integer numbers

print(result)

# The problem with this, is that we cant add decimal numbers, so in order to give as input any number we use float as below:

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)

print(result)