# class stud:
#     x="Anu"
# y=stud()
# print(y.x)
# class person:
#     def __init__(self,name,age) -> None:
#         self.name=name
#         self.age=age
# p=person("Anu",20)
# print(p.name,p.age)
# class a:
#     pass

class person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    def sub(self):
        print(self.name)
        print(self.age)
class student(person):
    pass
y=student("Anu",20)
y.sub()
