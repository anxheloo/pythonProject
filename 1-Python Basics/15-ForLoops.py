#For Loops

friends = ["Jim","Karen","Kevin"]


for letter in "Giraffe Academy":    #This prints out letter by letter
    print(letter)


for friend in friends:    #print every element on that array
    print(friend)


for index in range(10):   #print out numbers from 0-10 , exluding 10
    print(index)


for index in range(3,10):   #print out numbers from 3-10 , exluding 10
    print(index)


for index in range(len(friends)):   #give us a range from 0-3(excluding 3) | len(friends) is to find the length of friends which is 3.
    print(index)


print(len(friends))  #printing the length of our list

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not first")


print("Jim" in friends)  #to check if an element exist in the list, this will print true cuz Jim exist on the list

