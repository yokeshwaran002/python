class person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def getterage(self):
        return self.__age
    def setterage(self, age):
        self.__age=age
a=person("Yogesh",19)
print(a.getterage())
a.setterage(20)
print(a.getterage())