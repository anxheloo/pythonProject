
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
