fruits=["apple","orange","grape","mango","pineapple"]
print(fruits)
print(len(fruits))
print(type(fruits))
a=list((10,30,50,70))
print(a)
print(fruits[1])
print(fruits[-1])
print(fruits[1:3])
print(fruits[:5])
print(fruits[1:])
print(fruits[-3:-1])
print("orange" in fruits)
print("guva" not in fruits)
print("guva" in fruits)
print("orange" not in fruits)
fruits[2]="banana"
print(fruits)
fruits[2:4]="blueberry","guva"
print(fruits)

a.append(40)
print(a)
a.insert(1,90)
print(a)
fruits.extend(a)
print(fruits)
fruits.remove("blueberry")
print(fruits)
fruits.pop(3)
print(fruits)
fruits.pop()
print(fruits)
del fruits[-1]
print(fruits)
# fruits.clear()
# print(fruits)
# del fruits
# print(fruits)
for i in fruits:
    print(i)
clr=["red","orange","blue","green","yellow"]
print(clr)
clr.sort()
print(clr)
clr.sort(reverse=True)
print(clr)
y=clr.copy()
print(y)
z=list(a)
print(z)
x=a+z
print(x)

list1=["a","b","c"]
list2=[1,2,3,1]
for i in list2:
    list1.append(i)
print(list1)
d=list2.count(1)
print(d)