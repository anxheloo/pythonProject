# Reading & Writing

# Write,read
file = open("demo.txt", 'w')  # create the file
file.write("This is the text written to the file")  # write inside file
file.close()

file = open("demo.txt", 'r')  # open the file with read permission
content = file.read()  # we store the content in a variable to print it on terminal
print(content)
file.close()

file = open("demo.txt", 'w')  # we open the file again with write permission
file.write("This is second line")  # we add a second line,
file.close()

file = open("demo.txt", 'r')  # we read the file again
content = file.read()  # we store the content in a variable to print it on terminal
print(content)
file.close()

file = open("demo.txt", 'a')  # open the file with appended permission
file.write("\nTHis is the appended line")  # we add this line
file.close()



