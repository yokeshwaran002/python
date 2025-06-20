#add name list
'''names=[]
new_name=["yokesh","suba","riya","geetha","priyanga"]
for x in new_name:
    names.append(x)
    print(x)'''
#input add name list
'''names=[]
for x in range(5):
    name=input("Enter you Name:")
    names.append(name)
print(names)'''
#name,age,phone number.list
'''name=[]
age=[]
number=[]
for x in range(2):
    i1=input("Enter you Name:")
    i2=int(input("Enter you Age:"))
    i3=int(input("Enter you number :"))
    if(i2>=21):
        name.append(i1)
        age.append(i2)
        number.append(i3)
print('Name:',name)
print("Age:",age)
print("Number:",number)
if True:
    print('You must complet "21"')'''

'''name=[]
for x in range(2):
    o1=input("Enter you Name:")
    o2=int(input("Enter you Age:"))
    o3=int(input("Enter you number:"))
    name.append([o1,o2,o3])
for x in name:
    print(x)'''

name=[]
for x in range(2):
    o1=input("Enter you Name:")
    o2=int(input("Enter you Age:"))
    name.append([o1,o2])
    if(o2<18):
        name.pop(0)
for x in name:
    print(x)
















































