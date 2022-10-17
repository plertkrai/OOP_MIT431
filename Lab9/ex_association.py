"""
Name: {Puriwat Lertkrai}
SID: {11111111111}
Group: {MIT431}
"""

class Student:
    lst_teacher = list()
    def __init__(self,name,age,major,gpa):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa

    def student_info(self):
        print(f'Name: {self.name} Age: {self.age} '
              f'Major: {self.major} '
              f'GPA: {self.gpa}')

    def add_advisor(self,Teacher):
        self.lst_teacher.append(Teacher)
    def advisor_info(self):
        print(f'My Teacher following:')
        for x in self.lst_teacher:
            print(f'\t {x.name}')

class Teacher:
    lst_student = list()
    def __init__(self,name):
        self.name = name

    def teacher_info(self):
        print(f'Name: {self.name}')

    def add_student(self,Student):
        self.lst_student.append(Student)

    def student_info(self):
        print("My students following: ")
        for x in self.lst_student:
            #print(f'\t {x.student_info()}')
            x.student_info()

# create object
s1 = Student("Puriwat",36,"MIT",3.00)
s2 = Student("Piyapong",39,"MIT",3.50)

t1 = Teacher("Phornprasort")
t2 = Teacher("Nattapong")

# association
s1.add_advisor(t1)
s1.add_advisor(t2)
s1.student_info()
s1.advisor_info()

t1.add_student(s1)
t1.add_student(s2)
t1.teacher_info()
t1.student_info()