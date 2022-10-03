"""
Name: {Puriwat Lertkrai}
SID: {11111111111}
Group: {MIT431}
"""

class Person:
    def __init__(self,id,name):
        self.__id = id # private member
        self.__name = name
        self._nation = "Thai" # protected member
    # getter and setter method
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def person_info(self):
        print(f'I am Person ID:{self.__id} '
              f'Name: {self.__name} '
              f'Naiton: {self._nation}')

class Student(Person):
    def __init__(self,id,name,uni):
        self.uni = uni
        Person.__init__(self,id,name)
    def student_info(self):
        print(f'I am student, ID: {self.get_id()} '
              f'Name: {self.get_name()} '
              f'Nation: {self._nation} '
              f'University: {self.uni}')

# create object
std = Student("001","Puriwat Lertkrai","RUTS")
print(std.get_id())
print(std.get_name())

p = Person("002","Piyapong Senanut")
print(p.get_id())
print(p.get_name())

std.student_info()
p.person_info()