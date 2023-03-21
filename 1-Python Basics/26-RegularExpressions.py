import re           # -> this is the module we need to import for regular expressions

#We can use it to verify if the user input is correct and follows the pattern


pattern = r"eggs" # -> r is used for raw string,  the string should contain/start with 'eggs'

#this search for the pattern in the beggining of the string. The string below doesnt starts with eggs so "not found" is printed
if re.match(pattern,"baconeggseggsbacon"):
    print('Match found!')
else:
    print('No match found!')


#This search for the pattern anywhere in the string. 'Eggs' exist inside the string so 'Match found' is printed
if re.search(pattern,'baconeggseggsbacon'):
    print('Match found!')
else:
    print('Match not found!')

#How many times the pattern is visible in the string
print(re.findall(pattern,'baconeggseggsbacon'))


#                 FIND AND REPLACE
#Check for a match, if it exist, replace it with another string

string = "My name is John, Hi I'm John"
pattern = r"John"
newstring = re.sub(pattern,"Rob",string)   # 1- argument is for the pattern we are looking,
                                           # 2- is for the string we want to use instead of the match
                                           # 3- is for the string we are looking into
print(newstring)



#                THE "."(DOT) METACHARACTER

pattern2 = r"gr.y"    #we define a pattern which starts with 'gr' and ends with 'y'.
                      # THe "." we used in the pattern2 says that we can have any character there

if re.match(pattern2,"gray"):
    print("Match found!")




#                THE CARET AND DOLLAR METACHARACTER

pattern3 = r"^gr.y$"           # ^ -> signifies the starting point of the string, &-> signifies the ending point of the string

if re.match(pattern3,"grby"):
    print("Match 1 ")


#                CHARACTER CLASS

#Format of our apartment name is AA1 , character,character,number
pattern4 = r"[A-Z][A-Z][0-9]"

if re.search(pattern4,"AA1"):   #this string("AA1") matches with the pattern we have.
    print('Match found!')


#                STAR METACHARACTER

pattern5 = r"eggs(bacon)*"    #the bacon can be repeted multiple times or we can have no bacon at all. But "eggs" string is necessary

if re.match(pattern5,"eggsbaconbacon"):
    print("match found!")



#                 GROUP

pattern6 = r"bread(eggs)*bread"   #between this "breads" we can have 0-multiple eggs.

if re.match(pattern6,"breadeggseggsbread"):
    print("Match founddd")

