# List functions

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Beqo", "Liri Ketit"]

# extend the list by adding the lucky_numbers list
friends.extend(lucky_numbers)

# We can also add elements this way
friends = friends + ['how', 'are', 6, 'you']
print(friends)

# append(shtoj) an item in the list
friends.append("Creed")

# add an item in the middle of the list, at index 1. All other elemetns will be pushed next
friends.insert(1, "Kelly")


# remove element "Liri Ketit"
friends.remove("Liri Ketit")

# remove the last element of the list
friends.pop()

#remove element at index 3
del friends[3]
print(friends)

# remove all elements from the list
friends.clear()

# print(friends.index("Kevin"))  # print the index of the word "kevin" in our list/ check if element "Kevin exist in our list"

numbers = list(range(10)),  # this is a list with 10 numbers with a range of numbers from 0-9
numbers = list(range(3, 8)),  # this is a list with 5 numbers with a range from 3-8 (excluding 8)
numbers = list(range(1, 100, 5))  # this is a list of numbers from 1-100(excluding 100), but with an interval of 5 digits: 1,6,11,16,21....etc


print(friends.count("Jim"))  # how many times same element get shown


# Sort by alphabetic order/ also same for numbers, will sort them in ascending order
sorting = ["miri", "beqo", "liri", "anxhelo"]
sorting.sort(),  # -> To sort in descending order, we set the reverse = True for example: sorting.sort(reverse = True)
print(sorting)

lucky_numbers.reverse()  # reverse the list
print(lucky_numbers)

#Way 1 - Copy the list
friend2 = friends.copy()  # This will copy the friends list
                          # If we make it simple:  'a = friends', it will point to friends so if we change 'a' it will also change friends
#Way 2 - Copy the list
a = [1, 2, 3, 4]
b = list(a)

print(len(friends))  # print the length of the list

print("Kevin" in friends)  # print True, since Kevin exist on the list

# Filter function -> filter out the data from the list

newlist = [1, 3, 4, 5, 7, 2, 9, 11, 13, 6]
result = list(filter(lambda x: x % 2 == 0, newlist))

print(result)  # -> it prints even numbers

# index() function to print the index of an element inside a list
my_list = ['apple', 'banana', 'orange', 'grape']
index = my_list.index('banana')
print(f"The index of '{'banana'}' in the list is: {index}")



#We can also create a List that stores another List,Tuple,Set and a Dictionary inside

ourList = [1,2,3,4]     #we create a list
ourTuple = (1,2,3,4)    #we create a tuple
ourSet = {1,2,3,4}      #we create a set
ourDictionary = { 'list' : ourList, 'tuple' : ourTuple, 'set' : ourSet }    #we create a dictionary that stores 3 above

mainList = [ourList,ourTuple,ourSet,ourDictionary]      #we create a list that stores all of the above

print(mainList)             #print all elements of the mainList
print(mainList[0])          #print only the list inside mainList -> it is located at index 0 of our mainList
print(mainList[1])          #print only the tuple
print(mainList[2])          #print only the set
print(mainList[3])          #print only dictionary

print(mainList[0][1])       #print first element of the list inside the mainList
print(mainList[1][1])       #print 1 element of the tuple inside mainList
print(mainList[2])
print(mainList[3]['list'][1])   #print 1 element of the list, inside dictionary,  inside our mainList
