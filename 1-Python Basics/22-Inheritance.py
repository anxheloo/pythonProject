
'''
To model the idea of inheritance in real world, thats supoze we have a company that have employees and managers with different roles.
First we create a parent class that have the main attributes for both.
Than we create the child class of employee and manager, we reference the parent class with the super() keyword for the main attributes and
than we add the specific ones.

That is the idea of inheritance.
'''

class Pet:

    GRAVITY = 9.8
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    def speak(self):
        print("I dont know what I say")
    @classmethod
    def gravity(cls):               # this cls, references to the attributes of the class without needing an instance , same as self,
        return cls.GRAVITY          # but self reference to attributes of the class that are used inside constructors
    @staticmethod
    def add(x):
        return x + 5



class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)   #super() keyword references the parent class
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")


class Dog(Pet):
    def speak(self):
        print("Bark")



p = Pet("Tim", 19)
p.speak()
c = Cat("Bill", 34, "Brown")
c.show()
d = Dog("Jill", 25)
d.speak()

print(Pet.gravity())
print(Pet.add(5))