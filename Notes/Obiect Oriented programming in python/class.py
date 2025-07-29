'''class student:
    def __init__(yogesh,name,age,place):
        yogesh.name=name
        yogesh.age=age
        yogesh.place=place
    def display(yogesh):
        print(f"Name:{yogesh.name}\nAge:{yogesh.age}\nPlace:{yogesh.place}")
stu=student("Yogesh",20,"myd")

stu.display()'''

class office:
    def __init__(employee,name,email,phone,place,employee_id,skills,):
        employee.name=name
        employee.email=email
        employee.phone=phone
        employee.place=place
        employee.employee_id=employee_id
        employee.skills=skills
    def display(employee):
        print(f"Name:{employee.name}\nEmail:{employee.email}\nPhone:{employee.phone}\nPlace:{employee.place}\nId:{employee.employee_id}\nSkill:{ employee.skills}")
class student:
    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place=place
    def display(self):
        super(). __init__(name,email,phone,place)
ofe=office("yokesh","abc123@.gmail.com",9876543210,"myd","ABC002","Python")
ofe.display()
