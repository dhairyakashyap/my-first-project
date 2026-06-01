class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says WOOF!")
    
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says MEOW!")

dog = Dog("Bruno")
cat = Cat("Whiskers")
dog.speak()
cat.speak()
class GuideDog(Dog):
    def guide(self):
        print(f"{self.name} is guiding someone")

guide = GuideDog("Max")
guide.speak()
guide.guide()