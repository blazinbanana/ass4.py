class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}")

    #create an instance of the Person class
person1= Person("John",30,"male")
    
#call the introduce method to display the pserson's information

person1.introduce()