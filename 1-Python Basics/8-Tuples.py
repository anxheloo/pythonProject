#Working with Tuples  -> a container where we can store different values /same as lists but instead of [] we use ()
#once you create the tuple, we cant change it anymore, cant add, cant remove


coordinates = (4,5)

print(coordinates)

#Access Elements by index
print(coordinates[0])
print(coordinates[1])

list_of_coordinates = [(4,5),(6,7),(80,34)]   #list of tuples
print(list_of_coordinates)


T = (1,2,3,4,5,6)

#We can also slice tuples
print(T[:3])


T2 = ('a','b',45)

#Concatenate 2 Tuples
T3 = T + T2
print(T3)

#We delete the whole Tuple
del T3






