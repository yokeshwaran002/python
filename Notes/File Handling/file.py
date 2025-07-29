#open("file.txt","x")
'''
file=open("file.txt","w")
file.write("write something")
file.close()
  
file=open("file.txt","a")
file.write("write nothing")
file.close()

file=open("file.txt","r")
a=file.read()
print(a)
file.close()'''
#---------------------------------------------
#register
'''
file=open("file.txt","a")
name=input("Enter your name: ")
password=input("Enter your password: ")
file.write(name + "\t" + password + "\n")
file.close()
'''
#login
name=input("Enter your user name: ")
password=input("Enter your password: ")
file=open("file.txt","r")
a=file.read().split("\n")

for i in a:
    i= i.split("\t")
   
    if name==i[0] and password==i[1]:
        print("Login successful")
        break
else:
        print("Login failed")
file.close()
