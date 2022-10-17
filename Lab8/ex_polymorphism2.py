"""
Name: {Puriwat Lertkrai}
SID: {11111111111}
Group: {MIT431}
"""

# polymorphism and inheritance
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f'My name is {self.name},'
              f' I am {self.age} years old.')

class Teacher(Person):
    def __init__(self,name,age,major):
        super().__init__(name, age)
        self.major = major

    def introduce(self):
        print(f'My name is {self.name},'
              f' I am {self.age} years old.'
              f'I am teaching in {self.major} major.')

class Student(Person):
    def __init__(self,name,age,major):
        super().__init__(name,age)
        self.major = major
    def introduce(self):
        print(f'My name is {self.name},'
              f' I am {self.age} years old.'
              f'I am studying in {self.major} major.')

# create object

p = Person("Puriwat Lertkrai", 36)
t = Teacher("Piyapong Seananut",38,"MIT")
s = Student("Pornprasert Tipsawat",37,"AC")

department = [p,t,s]

for x in department:
    x.introduce()