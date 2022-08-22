"""
Name: {}
SID: {}
Group: {}
"""

"""
เขียนโปรแกรมไพธอนเพื่อนำเลขบัตรประชาชนมาบวกกันเพื่อทำนายดวงชะตาดังนี้
• สร้างฟังก์ชันเพื่อหาผลรวมของเลขบัตรประชาชน โดยใช้ชื่อฟังก์ชั่นว่า sumPID()
• สร้างฟังชั่นชื่อ getFortune() เพื่อทำนายดวงชะตา ถ้าเป็นเลขคู่ให้ทำนายว่า your fortune is good
• ถ้าเป็นเลขคี่ ให้ทำนายว่า your fortune is very good

ใช้ฟังก์ชั่น split()
"""

pid = input("Enter your pid: ")
#print(pid)

l_pid = [] # empty list

for x in pid:
    l_pid.append(int(x))
#print(l_pid)

l_pid2 = [int(x) for x in pid]
#print(l_pid2)

def sumPID(pid):
    s = 0
    for x in pid:
        s += x
    #print(s)
    return s

def getFortune(sumpid):
    if sumpid%2 ==0:
        print("Your fortune is good.")
    else:
        print("Your fortune is very good")

def getFortune2(sumpid):
    print("Your forturn is good.") if sumpid%2 == 0 else print("Your forturn is very good.")

sumpid = sumPID(l_pid)
getFortune(sumpid)
getFortune2(sumpid)