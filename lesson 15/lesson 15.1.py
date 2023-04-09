class Person():
    def __init__(self,firtname,lastname,age):
        self.firtname = firtname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.firtname} {self.lastname} and I’m {self.age} years old")


greeting = Person('Vadim','Kruk',24)
greeting.talk()





