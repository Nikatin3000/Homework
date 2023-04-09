class Dog:
    age_factor = 7
    def __init__(self,age_dog):
        self.age_dog = age_dog

    def human_age(self):
        return self.age_dog * Dog.age_factor



d = Dog(10)
print(d.human_age())



