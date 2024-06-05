import os
a=open("tsk1.txt","x")
a.close()
a=open("tsk1.txt","w")
a.write("good morning all ")
a.close()
a=open("tsk1.txt","r")
print(a.read())
print(a.read(5))
print(a.readline())
a.close()
a=open("tsk1.txt","a")
a.write("how are uh")
a.close()
b=open("tst2.txt","x")
os.remove("tst2.txt")
os.rmdir("sampllle")



a=open("tsk1.txt","r")
k=a.read()
print(k)
a.close()
a=open("tsk3.txt","w")
a.write(k)
a.close()
x=open("tsk3.txt","r")
print(x.read())








