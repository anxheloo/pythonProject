
class Students:

    #we create the object of the class student
    def __init__(self,name,contact):
        self.name = name
        self.contact = contact


    def getdata(self):
        print('Accepting data')
        self.name = input("Enter name: ")
        self.contact = int(input("Enter contact:"))


    def putdata(self):
        print('The name is: '+self.name ,' ,This is the contact: '+str(self.contact))



class ScienceStudent(Students):      #inherit from Students class

    def __init__(self,age):
        self.age=age


    def science(self):
        print("I am a science student!")


Rob = ScienceStudent(20)
Rob.science()

#We inherit methods from Students class and use in our ScienceStudent class
Rob.getdata()
Rob.putdata()

