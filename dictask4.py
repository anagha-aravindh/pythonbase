aha={"name":"anesh","age":22,"place":"payamal"}
print(aha)
print(type(aha))
print(len(aha))
bha=dict(name="ajay",age=44,job="mechanic")
print(["age"])
print(aha.get("name"))
xyz=aha.keys()
print(xyz)
xyh=aha.items()
print(xyh)
print("anesh" in aha)
print("anesh" not in aha)
aha["name"]="aji"
print(aha)
aha.update({"job":"supervisor"})
print(aha)
aha.update({"place":"thrissur"})
print(aha)
aha["DOB"]="3-10-2001"
print(aha)
aha.pop("DOB")
print(aha)
aha.popitem()
print(aha)
del aha["age"]
print(aha)
# aha.clear()
# print(aha)
# del aha
# print(aha)
for i in aha:
    print(i)
for i in aha:
    print(aha[i])
for i in aha.keys():
    print(i)
for i in aha.values():
    print(i)
for i in aha.items():
    print(i)
xyz=aha.copy()
print(xyz)
yzx=dict(xyz)
print(yzx)
homee={"childa":{"name":"ajuu","age":25},"childb":{"name":"biji","age":40},
        "childc":{"name":"ciju","age":58}}
print(homee)
print(homee["childb"]["age"])
print(homee["childc"]["name"])