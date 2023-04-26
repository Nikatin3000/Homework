class Person:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def name_person(self):
        return f"My name is {self.name}"

class Student(Person):
    def __init__(self, name, age, position, exam, scholarship):
        super().__init__(name, age, position)
        self.exam = exam
        self.scholarship = scholarship

class Teacher(Person):
    def __init__(self,name, age, position, salary, experiance):
        super().__init__(name, age, position)
        self.salary = salary
        self.experiance = experiance

st = Student('Vadim','24','student','2','1000')
print(st.name_person())
