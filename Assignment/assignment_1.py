"""
Name: {Puriwat Lertkrai}
SID: {11111111111}
Group: {MIT431}
"""

# ประกาศตัวแปร x มีค่าเท่ากับ 100
x =100
# แสดงผลค่าตัวแปร x
print(x)
# แสดงชนิดข้อมูลของตัวแปร x 
print(type(x))
# ประกาศตัวแปร  y มีค่าเท่ากับ 200
y = 200
# แสดงผลค่าตัวแปร y
print(y)
# แสดงชนิดข้อมูลของตัวแปร y 
print(type(y))
# แสดงผลค่าตัวแปร x และ y โดยมีข้อความดังนี้  "x is 100 and y is 200" 
print(f"x is {x} and y is {y}")
# หาผลรวมของตัวแปร x และ y และเก็บไว้ในตัวแปร z
z = x+y
# แสดงผลค่าตัวแปร z โดยการใช้ formatted print  -- > print(f{...}) z =
print(f'z = {z} and type of z is {type(z)}')

# หาผลลบของตัวแปร x และ y และเก็บไว้ในตัวแปร z
z = x-y
# แสดงผลค่าตัวแปร z formatted print  -- > print(f{...})
print(f'z = {z} and type of z is {type(z)}')
# หาผลคูณของตัวแปร x และ y และเก็บไว้ในตัวแปร z
z = x*y
# แสดงผลค่าตัวแปร z formatted print  -- > print(f{...})
print(f'z = {z} and type of z is {type(z)}')
# หาผลหารของตัวแปร x และ y และเก็บไว้ในตัวแปร z
z = x/y
# แสดงผลค่าตัวแปร z formatted print  -- > print(f{...})
print(f'z = {z} and type of z is {type(z)}')
# หาผลหารแบบจำนวนเต็ม (floor division) ของตัวแปร x และ y และเก็บไว้ในตัวแปร z
z = x//y
# แสดงผลค่าตัวแปร z formatted print  -- > print(f{...})
print(f'z = {z} and type of z is {type(z)}')
