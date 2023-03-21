from itertools import count,accumulate,takewhile

#same as range() function
for i in count(3):
    print(i)

    if i >=20:
        break

#Takes the previous numbers and current number and add them together
numbers = list(accumulate(range(8)))
print(numbers)

#Takewhile from itertools
print(list(takewhile(lambda x: x<=10,numbers)))