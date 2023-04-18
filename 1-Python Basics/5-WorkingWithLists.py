'''
Lists: ordered, mutable, allows dublicate elements, can hold different data types.
'''
mylist = list()
print(mylist)

friends = ["Kevin","Karen","Jim","Beqo","Liri Ketit"]
print(friends)

print(friends[2])  #printing by index

print(friends[-1]) #by using negative index we access the list from the back of the list

friends[1] = "Mike" #change an element inside a list
print(friends)

#List slicing
print(friends[:-1])  #this prints the list without the last element
print(friends[1:])   #this prints elements from index 1 to the end
print(friends[0:3])  #access elements from index 0-3(excluding 3)
print(friends[0:6:2])#it is going to skip values by 2: It will print: Kevin, Jim, Liri Ketit

#Creating List with  Rules
list = [x**2 for x in range(10)]                        #->  This will print:  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
list2 = [x**2 for x in range(10) if x**2 % 2 == 0]       #->  This will print even numbers:  [0, 4, 16, 36, 64]


#String Formatting
#This is useful when we want to display some date
numbers = [4,5,6]
newString = "Date:{0}/{1}/{2}".format(numbers[0], numbers[1], numbers[2])
print(newString)

a = "{x}/{y}".format(x=100,y=200)
print(a)




#2D lists & Nested Loops

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid)  #print the hole 2d list

print(number_grid[0]) #print the first list in the 2d list in this case [1,2,3]

print(number_grid[0][2]) #print the number at index 2 of the list at index 0
