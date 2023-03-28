

def function(*args):
    sum = 0
    for i in range(len(args)):
        sum +=args[i]

    print(sum)


function(1,2,3,4)
