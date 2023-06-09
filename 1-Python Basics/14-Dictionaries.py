'''
Dictionaries -> Allows us to store information( key value pairs) , we refer to the value by the key.  We can store any type of data
'''

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    0: "Beqo"
}

# For each key in monthConversions, print the key and monthConversions[key] -> we get the value
for x in monthConversions:
    print(x,monthConversions[x])

# To copy the dictionary without simply pointing to an existing one:
mydict_copy = dict(monthConversions)


print(monthConversions["Nov"])        #we give the key, and we get the value
print(monthConversions.get("Dec"))    #we get the value but passing the key

print(monthConversions.get("123","This key does not exist"))    #If the key doesnt exist we print the message: "This key does not exist"

print("Dec" in monthConversions)      #get True or False by checking if the key "Dec" exist in our dictionary

print("Luv","Not a valid key")        #instead of printing none for non existing keys, we give that a dafault value instead of none

# Adding key: 1 -> with value "Newly Added"
monthConversions[1] = "Newly Added"
print(monthConversions)

# We change the value of key 1
monthConversions[1] = "newly"
print(monthConversions)

# Deleting the key 1 and its value from dictionary | This works by giving the key
del monthConversions[1]
print(monthConversions)

# Remove the last item from the dictionary
dictionary = {'monday': "gym", 'tuesday': "basketball"}
print('Just created: ', dictionary)
dictionary.popitem()
print(dictionary)

# We can also update our Dictionary using .update({}) function
monthConversions.update({2:'hey',"3":'ca bone'})
print(monthConversions)

my_dict = {'name':"Max", "age":28, "email":"max@xyz.com"} #1.creating a dictionary
my_dict2 = dict(name='Mary', age=27, city='Boston')  #2.creating another dictionary
my_dict.update(my_dict2)    #3.updating first dict with second dict
print('printing my_dict: ', my_dict)


# We can also create a Dictionary that stores a List, Tuple, or Set

ourList = [1,2,3,4]

ourTuple = (1,2,3,4)

ourSet = {1,2,3,4}

Dictionary = { 'list' : ourList, 'tuple' : ourTuple, 'set' : ourSet }


print(Dictionary['list'])       #Access our list by the key: 'list'
print(Dictionary['list'][1])    #Access our element at index 1 of our list by giving the key and the index

print(Dictionary['tuple'][1])   #Same with tuple


# Print all elements of the Dictionary
for x in Dictionary:
    print(x, Dictionary[x])
