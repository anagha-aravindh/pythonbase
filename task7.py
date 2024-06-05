# primeornot
n=int(input("enter a number:"))
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
    else:
        print("it is prime")
# # circle
# import math
# def circle(r):
#     cir=2*math.pi*r
#     return cir
# r=float(input("enter the radius:"))
# cir=circle(r)
# print(cir)
# # leapyear
# def leap(yr):
#     if yr%4!=0:
#         return False
#     elif yr%100!=0:
#         return True
#     elif yr%400!=0:
#         return False
#     else:
#         return True
# yr=int(input("enter a year:"))
# if leap(yr):
#     print("it is a leap yr")
# else:
#     print("it is not a leap yr")
# sphere
import math
r=int(input("enter the radius:"))
cir=4*math.pi*r
print(cir)