#Catching errors

try:
    number = int(input("Enter a number:"))
    print(number)
except:
    print("Invalid Input!")           #We are catching a general exception




try:
    value = 10 / 0
except ZeroDivisionError:
    print("Devided by zero not accepted!")    #We are catching ZeroDivisionError exception


#We can also store the error in a variable
try:
    value = 10 / 0
except ZeroDivisionError as err:
    print(err)
finally:
    print('This is going to execute no matter what')	#Catching or not catching errors , it is going to execute
