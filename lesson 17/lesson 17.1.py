class Animal:
    def talk(self):
        pass

class Cat(Animal):
    def talk(self):
        print('Meow!')

class Dog(Animal):
    def talk(self):
        print('Woof Woof!')

def animal_talk(animal: Animal):
    animal.talk()

dog = Dog()
cat = Cat()
animal_talk(dog)
animal_talk(cat)