'''#mulitiple inheritance
class student:
    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place
    def display(self):
        print(f"Name: {self.name}, Age: {self.age},Place: {self.place}")
class school(student):
    def __init__(self,name,age,place,schoolname,total,grade):
        super().__init__(name,age,place)
        self.schoolname = schoolname
        self.total=total
        self.grade=grade
    def display(self):
        super().display()
        print(f"School Name: {self.schoolname}, Total: {self.total}, Grade:{self.grade}")
stu=school("yogesh",20,"myd","sgfd",543,"A")
stu.display()'''

#multilevel inheritance
class grandparent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
class parent(grandparent):
    def __init__(self, name, age, place):
        super().__init__(name, age)
        self.place = place
    def display(self):
        super().display()
        print(f"Place: {self.place}")
class child(parent):
    def __init__(self, name, age, place, schoolname, total, grade):
        super().__init__(name, age, place)
        self.schoolname = schoolname
        self.total = total
        self.grade = grade
    def display(self):
        super().display()
        print(f"School Name: {self.schoolname}, Total: {self.total}, Grade:{self.grade}")
stu=child("yogesh",20,"myd","sgfd",543,"A")
stu.display()