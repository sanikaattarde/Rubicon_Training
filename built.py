# import math
#no=int(input("enter a no"))
# po=int(input("enter the power"))
# print(f"square root of {no} is",math.sqrt(no))
# print(f"factorial of {no} is",math.factorial(no))
# print(f"power of {no} is",math.pow(no,po))
# print(f"log of {no} is",math.log(no))
# print(f"sine of {no} is",math.sin(no))
# print(f"cosine of {no} is",math.cos(no))

#delivery distance finding
# x1,y1=4,2
# x2,y2=3,5
# print("distance is:",math.sqrt((x2-x1)**2 +(y2-y1)**2))

# calculating area(circle)
# r=int(input("enter radius:"))
# print("area of circle is:",math.pi*pow(r,2))

#EMI
# p=int(input("enter the principle amt:"))
# ra=int(input("enter the rate in % :"))
# r=ra/(100*12)
# n=int(input("enter no. of months:"))
# emi=(p*r*math.pow(1+r,n))/(math.pow(1+r,n)-1)
# print(emi)


# remaining days 
# from datetime import datetime,date
# event=datetime(2026,4,25)
# tod=datetime.now().time()
# remaining =event-today
# print("Remaining Days:", remaining.days)


# if tod.hour<12:
#     print("present")
# else:
#     print("absent")



#3. os module

import os 
# print(os.listdir())
# os.mkdir("sani")
# os.rmkdir("sani")
# os.rename("sani","sanu")
# os.path.exists("sanu")
# os.path.getsize("sanu")

for i in range(0,10):
    os.mkdir(f"folder{i+1}")
print(os.listdir())
