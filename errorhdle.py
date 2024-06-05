try:
    print(x)
except:
    print("error occured")

try:
    print(x)
except NameError:
    print("x is not defined")
except:
    print("it is defined")
try:
    x=20
    print(x)
except:
    print("error occured")
else:
    print("it is defined")
finally:
    print("finish")
y=-1
if y<0:
    raise Exception("no numbers below zero")


n=int(input("enter:"))
f=1
for i in range(1,n+1):
    f=f*i
print(n) 