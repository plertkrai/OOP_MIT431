"""
Name: {Puriwat Lertkrai}
SID: {11111111111}
Group: {MIT431}
"""

# Class relations - composition

class Faculty:
    def __init__(self,fac_name):
        self.fac_name = fac_name
    def fac_info(self):
        print(f'Faculty Name: {self.fac_name}')

class University:
    lst_faculty = list()

    def __init__(self,uniname):
        self.uniname = uniname
    def uni_info(self):
        print(f'University name: {self.uniname}')

    def get_faculty(self):
        f1 = Faculty("MT")
        f2 = Faculty("Sci")
        self.lst_faculty.append(f1)
        self.lst_faculty.append(f2)
    def fac_info(self):
        print(f"This {self.uniname} has faculty below:")
        for x in self.lst_faculty:
            x.fac_info()

# create object
u1 = University("RUTS")
u1.get_faculty()

# display data
u1.uni_info()
u1.fac_info()