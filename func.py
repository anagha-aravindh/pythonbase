def length():
    print("hello")
length()

def fab(*x):
    print(x[2])
fab(1,2,3,4)

def fact(x,y,z):
    print(x)
fact(x='string',y='king',z='var')

def sub(**x):
    print(x["string"])
sub(string='dog',a="b",c="lir")

def mycountry(country="india"):
    print(country)
mycountry("pakisthan")
mycountry("usa")
mycountry()

def pak(x):
    return 10+x
print(pak(4))

def add(x,y):
    return x+y
print(add(10,20))

def sub(x):
    pass

x=lambda a:a+10
print(x(20))

y=lambda a,b,c:a+b+c
print(y(10,20,30))