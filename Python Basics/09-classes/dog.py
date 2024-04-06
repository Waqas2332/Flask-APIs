class Dog():
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    
    def sit(self):
        print(self.name.title() + " is now sitting")
        
my_dog = Dog("tommy",7)

print(f"Name of my Dog is {my_dog.name.title()}")