'''
   Working with Tuples  -> a container where we can store different values /same as lists but instead of [] we use ()
   Once you create the tuple, we cant change it anymore, cant add, cant remove
'''


coordinates = (4,5)
print(coordinates)

if 4 in coordinates:
    print("Yes")
else:
    print("No")

# Count how many times number '4' exists:
print(coordinates.count(4))

#Access Elements by index
print(coordinates[0])
print(coordinates[1])
#Access Index by Element
print('Index of number 5 inside the Coordinates Tuple is: ', coordinates.index(5))

#list of Tuples
list_of_coordinates = [(4,5),(6,7),(80,34)]
print(list_of_coordinates)
print('Access the first tuple inside the list of tuples: ', list_of_coordinates[0])
print('Access the second element of the first tuple inside the list of tuples: ', list_of_coordinates[0][1])


T = (1,2,3,4,5,6)

#We can also slice tuples
print(T[:3])

T2 = ('a','b',45)

#Concatenate 2 Tuples
T3 = T + T2
print('Concatenate 2 Tuples: ', T3)

#We delete the whole Tuple
del T3






