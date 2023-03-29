#Dictionaries    -> Allows us to store informations( key value pairs) , we refer to the value by the key.  We can store any type of data

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

#For each key in monthConversions, print the key and monthConversions[key] -> we get the value
for x in monthConversions:
    print(x,monthConversions[x])



print(monthConversions["Nov"])        #we give the key, and we get the full name

print(monthConversions.get("Dec"))    #we get the value but passing the key

print(monthConversions.get("123","This key does not exist"))    #If the key doesnt exist we print the message: "This key does not exist"

print("Dec" in monthConversions)      #get True or False by checking if the key "Dec" exist in our dictionary

print("Luv","Not a valid key")        #instead of printing none for non existing keys, we give that a dafault value instead of none

#Adding key: 1 -> with value "Newly Added"
monthConversions[1] = "Newly Added"
print(monthConversions)

#We change the value of key 1
monthConversions[1] = "newly"
print(monthConversions)

#Deleting the key 1 and its value from dictionary | This works by giving the key
del monthConversions[1]
print(monthConversions)


#We can also update our Dictionary using .update({}) function
monthConversions.update({2:'hey',"3":'ca bone'})
print(monthConversions)


#We can also create a Dictionary that stores a List, Tuple, or Set

ourList = [1,2,3,4]

ourTuple = (1,2,3,4)

ourSet = {1,2,3,4}

Dictionary = { 'list' : ourList, 'tuple' : ourTuple, 'set' : ourSet }


print(Dictionary['list'])       #Access our list by the key: 'list'
print(Dictionary['list'][1])    #Access our element at index 1 of our list by giving the key and the index

print(Dictionary['tuple'][1])   #Same with tuple


#Print all elements of the Dictionary
for x in Dictionary:
    print(x, Dictionary[x])
