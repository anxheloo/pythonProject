# List functions

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Beqo", "Liri Ketit"]

friends.extend(lucky_numbers)  # extend the list by adding the lucky_numbers list
friends.append("Creed")  # append(shtoj) an item in the list
friends.insert(1, "Kelly")  # add an item in the middle of the list, at index 1. All other elemetns will be pushed next

friends.remove("Liri Ketit")  # remove element "Liri Ketit"
friends.pop()  # remove the last element of the list
friends.clear()  # remove all elements from the list

print(friends.index("Kevin"))  # print the index of the word "kevin" in our list/ check if element "Kevin exist in our list"

numbers = list(range(10)),  # this is a list with 10 numbers with a range of numbers from 0-9
numbers = list(range(3, 8)),  # this is a list with 5 numbers with a range from 3-8 (excluding 8)
numbers = list(range(1, 100,5))  # this is a list of numbers from 1-100(excluding 100), but with an interval of 5 digits: 1,6,11,16,21....etc

print(friends.count("Jim"))  # how many times same element get shown




# Sort by alphabetic order/ also same for numbers, will sort them in ascending order

sorting = ["miri", "beqo", "liri", "anxhelo"]
sorting.sort(),  # -> To sort in descending order, we set the reverse = True for example: sorting.sort(reverse = True)
print(sorting)

lucky_numbers.reverse()  # reverse the list
print(lucky_numbers)

friend2 = friends.copy()  # this will copy the friends list

print(len(friends))  # print the length of the list

print("Kevin" in friends)  # print True, since Kevin exist on the list




# Filter function -> filter out the data from the list

newlist = [1, 3, 4, 5, 7, 2, 9, 11, 13, 6]
result = list(filter(lambda x: x % 2 == 0, newlist))

print(result)  #-> it prints even numbers
