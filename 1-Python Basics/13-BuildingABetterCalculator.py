#Building a better calculator in python

num1 = input("Enter first number: ")
operator = input("Enter operator: ")

while operator != "*" and operator != "+" and operator != "/" and operator != "-":
    operator = input("Enter operator: ")

num2 = input("Enter second number: ")

if operator == "+":
    result = float(num1) + float(num2)      #instead of adding float here, we can concatinate the hole input field: num1 = float(input("Enter first number: "))
elif operator == "-":
    result = float(num1) - float(num2)
elif operator == "*":
    result = float(num1) * float(num2)
elif operator == "/":
    result = float(num1) / float(num2)

print(result)