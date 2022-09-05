from ex_class2 import MyPet


def test_fun():
    MyPet.display_all_mypet("")

def input_pet_data():
    name = input("Enter your pet name: ")
    age = int(input("Enter your pet age: "))
    breed = input("Enter your pet breed: ")

    return name,age,breed

data = input_pet_data()
p1 = MyPet(data[0],data[1],data[2])
p1.display_info()

data = input_pet_data()
p2 = MyPet(data[0],data[1],data[2])
p2.display_info()

print(f"I had {len(MyPet.mypet)} following: ")

#MyPet.display_all_mypet()
test_fun()
