class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hello,I am {self.name} and I am {self.age} years old.")

dhairya = Person("Dhairya",18)
dhairya.introduce()
friend = Person("Arjun",19)
friend.introduce()