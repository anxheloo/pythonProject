class Students:

    #we create the object of the class student
    def __init__(self,name,contact):
        self.name = name
        self.contact = contact

    #method 1
    def getdata(self):
        print('Accepting data')
        self.name = input("Enter name: ")
        self.contact = int(input("Enter contact:"))

    #method 2
    def putdata(self):
        print('The name is: '+self.name ,' ,This is the contact: '+str(self.contact))



John = Students("blank",694038597)
John.getdata()
John.putdata()
