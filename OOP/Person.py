from dataclasses import dataclass


@dataclass
class Dog:
    name: str
    age: int
    tricks: []  # string

    def bark(self):
        print(f'{self.name} BARKS!')

    def sit(self):
        print(f'{self.name} SITS!')


my_dog = Dog("Boots", 12, "sit" "bark")
my_dog.bark()
my_dog.sit()

class Person(Dog):
    p_name: str
    p_age: int
    pet: Dog

    def __init__(self):
        self.Dog = None

    def walk_dog(self):
        print(f"Dog is walked{self.Dog}")

ben = Person("Ben", 20, my_dog)
ben.walk_dog()

