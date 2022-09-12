"""
Name: {Puriwat Lertkrai}
SID: {11111111111}
Group: {MIT431}
"""

class MyPet:
    # class attribute
    mypet = []
    def __init__(self,name,age,breed):
        # object attributes
        self.name = name
        self.age = age
        self.breed = breed
        self.mypet.append(self)

    def display_info(self):
        print(f'Name: {self.name} Age: {self.age} Breed: {self.breed}')

