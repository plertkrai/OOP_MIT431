from labtop import Labtop


# display
def display_labtop():
    if len(my_labtop) ==0:
        print("\nYou had no labtop data.\n")
    else:
        num = 1
        print(f'You had {len(my_labtop)} following:')
        for x in my_labtop:
            print(f'{num}. ',end="")
            x.display_laptop()
            num +=1
        print("\n")

# option
def display_option():
    print("Welcome to Labtop Data Store System (LDSS)")
    print("1.Add Labtop")
    print("2.Display all Labtop")
    print("3.Delete Labtop")
    print("4.Edit Labtop price")
    print("5.exit")
    select = int(input("select(1-5)? : "))
    if select == 1:
        input_labtop_data()
    elif select==2:
        display_labtop()
    elif select == 3:
        delete_labtop()
    elif select == 4:
        edit_labtop_price()
    elif select ==5:
        print("Good Bye.")
        exit(0)
    else:
        print("Please, select number 1-5.")

# edit data
def edit_labtop_price():
    display_labtop()
    # length of my_laptop
    n = len(my_labtop)
    s = 1
    while s:
        s = int(input(f"select 1-{n} or type 0 to main option: "))
        if s in range(1, n + 1):
            print(f'current price: {my_labtop[s-1].get_price()}')
            newprice = float(input("enter new price: "))
            my_labtop[s-1].set_price(newprice)
            print("\nAlready updated labtop data.\n")
            break
        elif s == 0:
            break
        else:
            print(f"Please,enter number 1-{n} or type 0 to main option: ")

# delete data
def delete_labtop():
    display_labtop()
    # length of my_laptop
    n = len(my_labtop)
    s =1
    while s:
        s = int(input(f"select 1-{n} or type 0 to main option: "))
        if s in range(1,n+1):
            my_labtop.pop(s-1)
            print("\nAlready deleted labtop data.\n")
            break
        elif s == 0:
            break
        else:
            print(f"Please,enter number 1-{n} or type 0 to main option: ")



# input data
def input_labtop_data():
    brand = input("Enter labtop brand: ")
    model = input("Enter labtop model: ")
    cpu = input("Enter labtop cpu: ")
    ram = int(input("Enter labtop ram:"))
    display= float(input("Enter display size: "))
    storage= int(input("Enter size of storage: "))
    price = float(input("Enter price: "))

    #return brand,model,color,maxspeed,price # return as tuple
    my_labtop.append(Labtop(brand,model,cpu,ram,display,storage,price))

    print("\n-----------------------------------")
    print("Already add Labtop to store.")
    print("\n-----------------------------------")

my_labtop = []
my_labtop.append(Labtop("ASUS","Vivobook",
                        "Intel Core i5-12500H",
                        8,15.6,512,27990))
my_labtop.append(Labtop("Lenovo","IdeaPad Gaming 3",
                        "Intel Core i5-11320H",
                        8,15.6,512,25990))
s = 0
while s == 0:
    display_option()