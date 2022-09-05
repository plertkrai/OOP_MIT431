"""
Name: {Puriwat Lertkrai}
SID: {11111111111}
Group: {MIT431}
"""

# create class
class Student:
    # class attribute
    university = "RUTS"
    mystudent = [] # list

    def __init__(self,name,major):
        # object attributes
        self.name = name
        self.major = major
        self.mystudent.append(self)

    def __str__(self):
        print(f'My name is {self.name}, I am studying in {self.major}')


# create object
s1 = Student("Puriwat Lertrai","MIT")
s2 =Student("Piyapong Senanut","AC")

print(s1.name, s1.major)
print(s2.name, s2.major)

s1.major = "LM"
print(s1.name, s1.major)

# access to class attribute
print(s1.name,s1.university)
print(s2.name,s2.university)

s1.university = "Saiyai"

print(s1.name,s1.university)
print(s2.name,s2.university)

Student.university = "Thungsong"

print(s1.name,s1.university)
print(s2.name,s2.university)

Student.university = 'Test'
print(s1.name,s1.university)
print(s2.name,s2.university)

print(len(Student.mystudent))


s1.__str__()
s2.__str__()
