#---------------------------------------------
#read file
'''file=open("file.txt","r")
a=file.read()
print(a)
file.close()'''
#---------------------------------------------
#write file
'''file=open("file.txt","w")
file.write("write something")
file.close()
file=open("file.txt","r")
a=file.read()
print(a)
file.close()'''
#---------------------------------------------
#append file
'''file=open("file.txt","a")
file.write("write nothing")
file.close()
file=open("file.txt","r")
a=file.read()
print(a)
file.close()'''
#---------------------------------------------
#read file line by line
'''file=open("file.txt","r")
for i in file:
    print(i)
file.close()'''
#---------------------------------------------
#read file line by line with split
'''file=open("file.txt","r")
for i in file:
    i=i.split("\t")
    print(i)
file.close()'''     
#---------------------------------------------
#read file line by line with split and strip
'''file=open("file.txt","r")
for i in file:
    i=i.split("\t")
    i=[x.strip() for x in i]
    print(i)
file.close()'''
#---------------------------------------------
#read file line by line with split and strip and append to list
'''file=open("file.txt","r")
data=[]
for i in file:
    i=i.split("\t")
    i=[x.strip() for x in i]
    data.append(i)
file.close()
print(data)'''
#---------------------------------------------
#read file line by line with split and strip and append to list with dictionary
'''file=open("file.txt","r")
data=[]
for i in file:
    i=i.split("\t")
    i=[x.strip() for x in i]
    data.append({"name":i[0],"password":i[1]})
file.close()
print(data)'''
#---------------------------------------------
#read file line by line with split and strip and append to list with dictionary and check login
file=open("file.txt","r")
data=[]
for i in file:
    i=i.split("\t")
    i=[x.strip() for x in i]
    data.append({"name":i[0],"password":i[1]})
file.close()
name=input("Enter your user name: ")
password=input("Enter your password: ")
for i in data:
    if name==i["name"] and password==i["password"]:
        print("Login successful")
        break
else:
    print("Login failed")
#---------------------------------------------
#read file line by line with split and strip and append to list with dictionary and check login with function

def check_login(name, password):
    for i in data:
        if name == i["name"] and password == i["password"]:
            return True
    return False
`````