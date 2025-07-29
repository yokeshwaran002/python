from abc import ABC,abstractmethod
class student(ABC):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @abstractmethod
    def display(self):
        print(f"Name:{self.name} Age:{self.age}")
class school(student):
    def __init__(self, name, age,place):
        super().__init__(name, age)
        self.place=place
    def display(self):
        super().display()
        print(f"Place:{self.place}")
stu=school("Yogesh",20,"myd")
stu.display()