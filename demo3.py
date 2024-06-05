a="hello"
print(a)
print(type(a))
print(len(a))
print(a[1])
for i in a:
    print(i)
y="  python is, a programming, language  "
print(y)
print("is " in y)
print("be" not in y)
print(y[2:5])
print(y[:5])
print(y[11:])
print(y[-1])
print(y[-5:-2])
print(y.upper())
print(y.lower())
print(y)
print(y.strip())
print(y.replace('p','h'))
print(y.split(','))
print(a+y)
print(a+""+y)
age=30
text="my name is john and i am {}"
# print(text+age)
print(text.format(age))
txt="i have {} apples and the amount is {} for each"
sum=20
amt=100
print(txt.format(sum,amt))
ste="i love apple and apple is a fruit"
print(ste.count("apple"))
