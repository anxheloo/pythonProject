#Sets - it does not allow dublicate elements, different from lists we use curly braces

numbers = {1,2,3,4,5,6}
print(numbers)

#check if 5 is present in the set, True or False
print(5 in numbers)

#add a number to the set
numbers.add(9)
print(numbers)

numbers.update({'home','house'})
print(numbers)

#remove any element we specify by using index number or the value inside the Set
numbers.remove(4)
numbers.remove("home")
print(numbers)

#union elements of 2 sets with no dublicate entries
setA = {1,2,3,4,5}
setB = {4,5,6,7,8}
print(setA | setB)

#we print the elements that are common in both sets
print(setA & setB)

#substract setB from setA - removes elements of setB and common elements of setA that are in setB, so we get 1,2,3
print(setA - setB)



