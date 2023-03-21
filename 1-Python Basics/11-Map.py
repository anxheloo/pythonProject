#Map - A map allows us to perform a single operation on a list

def add(x):
    return  x+2

newlist = [10,20,30,40,50]

result = list(map(add,newlist))

#using lambda instead of function
result = list(map(lambda x: x*2,newlist))

print(result)
