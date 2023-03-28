
L = [-1,-3,5,-7]


def findMin(L):
    min = L[0]
    idx = 0
    j=0

    for i in L:
        if i < min:
            min = i
            #So when we get our minimum value, we make idx = j, our idx is equal to 3
            idx = j

        #After each iteration we save the number
        j+=1

    print(min,idx)


findMin(L)