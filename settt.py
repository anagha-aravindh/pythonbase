x={'dog',1,'cat',2}
print(x)
print(type(x))
print(len(x))
y=set((10,20,30,40))
print(y)
for i in y:
    print(i)
print(1 in x)
print(10 not in x)
y.add(100)
print(y)
x.update(y)
print(x)
fruits=('banana','grapes','guva')
print(fruits)
x.update(fruits)
print(x)
x.remove('banana')
print(x)
x.discard('apple')
print(x)
x.discard("guva")
print(x)
g=x.pop()
print(g)
# x.clear()
# print(x)
# del x
j=y.union(x)
print(j)
k={10,20,30,40}
l={10,60,30,50}
n=k.intersection(l)
print(n)
n=k.difference(l)
print(n)