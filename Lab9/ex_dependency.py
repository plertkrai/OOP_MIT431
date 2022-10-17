"""
Name: {Puriwat Lertkrai}
SID: {11111111111}
Group: {MIT431}
"""

# class relations - dependency

from datetime import date

class Customer:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def customer_info(self):
        print(f'cusid: {self.id} cusname: {self.name}')

class Oder:
    def __init__(self,id,Customer,date,total_cost):
        self.id = id
        self.customer = Customer
        self.date = date
        self.total_cost = total_cost
    def oder_info(self):
        print(f'oder id: {self.id} '
              f'customer name: {self.customer.name} '
              f'date: {self.date} '
              f'total cost: {self.total_cost}')

# create object
customer1 = Customer("cus001","Puriwat Lertkrai")

order1 = Oder("order001",customer1,date.today(),15000.00)

# display data
customer1.customer_info()
order1.oder_info()