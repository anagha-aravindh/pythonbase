flwr=["rose","jasmine","lotus","lily","hibiscus"]
print(flwr)
print(type(flwr))
print(len(flwr))
z=list([20,40,60,80])
print(z)
print(flwr[1])
print(flwr[0:3])
print(flwr[:3])
print(flwr[1:])
print(flwr[-1])
print(flwr[-3:-1])
print("rose" in flwr)
print("daliya" not in flwr)
flwr[4]="daliya"
print(flwr)
flwr[1:3]="sunflower","hibiscus"
print(flwr)
z.append(30)
print(z)
z.insert(1,90)
print(z)
flwr.remove("hibiscus")
print(flwr)
flwr.pop(3)
print(flwr)
flwr.pop()
print(flwr)
# flwr.clear()
# print(flwr)
# del flwr
# print(flwr)
for i in flwr:
    print(i)
colr=["red","orange","blue","green","yellow"]
print(colr)
colr.sort()
print(colr)
for i in colr:
    print(i)
colr.sort(reverse=True)
print(colr)
a=colr.copy()
print(a)
b=list(a)
print(b)
d=flwr+z
print(d)
lstm=["a","b","c"]
lstn=[1,2,3,3,3,3]
for i in lstn:
    lstm.append(i)
print(lstm)
h=lstn.count(3)
print(h)