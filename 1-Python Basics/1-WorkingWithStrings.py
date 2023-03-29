print("Giraffe\nAcademy")  #it will print in new lines
print("hello "+"world")  #concatinate 2 strings

#To Concatenate a String and a Integer we need to convert our Integer to String:
print('String ' + str(12))
#Or use ','
print('String',12)


#we store the string hello inside phrase
phrase = "hello"

#Functions
print(phrase.upper())
print(phrase[0]) #this way we access the letter at index 0
print(phrase.index("e")) #this print 1, because the letter "e" is located at index 1 inside hello
print(phrase[1:3])  #we can also use slicing with strings
print(phrase[::-1])  #Reverse String

phrase = "hello"
print(phrase.startswith("h"))
print(phrase.endswith("o"))
print("The length of String phrase is: ",len(phrase))
print("ll" in phrase) #Check if "ll" is in the phrase


#Replace hello with hello world
print(phrase.replace("hello", "hello world"))
print("Hello There".replace("There","world"))


print("He\'s a good guy") , # \' or \"  is used to make the sign (') or (")

#String Formatting - This is useful when we want to display some date
numbers = [4,5,6]
newString = "Date:{0}/{1}/{2}".format(numbers[0], numbers[1], numbers[2])
print(newString)

a = "{x}/{y}".format(x=100,y=200)
print(a)


#String Multiline

print(''' The following options are available:
        -a      : does nothing
        -b      : also does nothing
        ''')

#Remove spaces at the Beggining and the End
a = "   A lot of Spaces at the     beginning and the end    "
b = a.strip()
print(b)
