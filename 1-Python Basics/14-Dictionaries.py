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

