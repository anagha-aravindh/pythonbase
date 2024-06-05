class animal:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    def sub(self):
        print(self.name)
        print(self.age)
class wild(animal):
    pass
x=wild("elephant",12)
x.sub()