from mypet import MyPet


# ใช้แสดงตัวเลือกให้ผู้เลือกการทำงาน
"""
1.เพิ่มข้อมูลสัตว์เลี้ยง
2.แสดงข้อมูลสัตว์เลี้ยง
3.ออกจากระบบ
"""
def display_option():
    print("\nPlease, select option below: ")
    print("1. add pet data.")
    print("2. display pets data.")
    print("3. exit.")

    b = True
    while b:
        select = int(input("select(1-3)? :"))
        if select ==1:
            input_mypet_data()
            display_option()
        elif select ==2:
            display_mypet()
            display_option()
        elif select ==3:
            print("Good Bye.")
            exit(0)
        else:
            print("Please, enter 1-3 only. Thank.\n")


# ใช้แสดงข้อมูลของสัตว์เลี้ยงทั้งหมด
def display_mypet():
    if len(mypet_list) ==0:
        print("You had no pet data.")
    else:
        count = 1
        print(f"Your had {len(mypet_list)} pet following: ")
        for x in mypet_list:
            print(f'{count}.',end=" ")
            f'{x.display_info()}'
            count += 1

# ใช้รับข้อมูลสัตว์เลี้ยงจากผู้ใช้
def input_mypet_data():
    name = input("Enter your pet name: ")
    age = int(input("Enter your pet age: "))
    breed = input("Enter your pet breed: ")
    mypet_list.append(MyPet(name,age,breed))
    print("Your pet data is already add to store....")


# list
print("---------------------------------------")
print("|  Welcome, to Pet data store system  |")
print("---------------------------------------")
mypet_list = []
display_option()


