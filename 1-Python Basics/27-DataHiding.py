class Myclass:

    __hiddenvariable = 0  #this will make the variable hidden and not able to access it outside this class
                          #we can only work with it inside the scope of the class

    def add(self,incerement):  #we used the hidden variable inside Myclass
        self.__hiddenvariable += incerement
        print(self.__hiddenvariable)


object1 = Myclass()   #we create the object, but still cant access the __hiddenvariable directly
object1.add(5)        #we call the method(which exist inside Myclass) within which we incremented the hiddenvariable

print(object1.__hiddenvariable)  #-> cant access it directly
