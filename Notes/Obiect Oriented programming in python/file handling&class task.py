
#open("details.txt","x").
class student:
    def __init__(yogesh,name,age,place):
        yogesh.name=name
        yogesh.age=age
        yogesh.place=place
    def display(yogesh): 
        print(f"Name:{yogesh.name}\nAge:{yogesh.age}\nPlace:{yogesh.place}")
stu = student("Yogesh", 20, "myd")
stu.display()
file=open("details.txt","a")
file.write(f"Name:{stu.name}\nAge:{stu.age}\nPlace:{stu.place}\n")
file.close() 