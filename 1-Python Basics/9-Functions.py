
#To create a function we use the def word and the name of the function after, colon and keeping the format as example
def sayHi():
    print("Hello User")

sayHi()

#Giving a parameter of name
def sayHi(name,age):
    print("Hello " + name + " you are " + age)  #or      print("Hello " + name + " you are " + str(age)) to convert the integer to string

sayHi("Anxhelo", "26")
sayHi("Anxhelo",str(26))
    #sayHi("Anxhelo", 26)   -> error


def cube(num):
    return num*num*num

print(cube(3))



#Function that takes as parameter a function
def add_ten(x):
    return x+10

def twice(func,args):
    return func(func(args))     #-> this function should add the parameter twice, in this case "10"

print(twice(add_ten,10))



print()


#Multi Argument Function
def function(*args):
    sum = 0
    for i in range(len(args)):
        sum +=args[i]

    print(sum)


function(1,2,3,4)



print()

#Multi Arguments With Keywords and Values
def printAllVariableNamesAndValues(**args):
    for x in args:
        print("Variable Name is: ",x, " And value is :",args[x])


printAllVariableNamesAndValues(a = 3, b = "B", c = "CCC", y = 6.7)