
#Seprators
'''
print("Hello","World")
print("Hello","World",sep=("@#%$%^%"))
print("Hello","World!",sep=("\n"))
print("Hello","World",sep=("\t"))
'''
#Data Types
'''
a='i'
b=123
c=56.5
d=2+0j#complex
'''
#String
'''
a='"python" programming'
print(a)
b="Good 'Evening'"
print(b)
c="I am a \"programmer\""
print(c)
d='I am a \'Programmer\''
print(d)

txt="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(txt)
'''
#Length
'''
name="Jack"
print(len(name))
'''
#Slice
'''
str1="Python Programming"
print(len(str1))
print(str1[10])
print(str1[4:12])
print(str1[:10])
print(str1[4:])

print(str1[-6:-2])
print(str1[:-12])
print(str1[-11:])

m="livEwirE prograMminG for All"
print(m.upper())
print(m.lower())
print(m.title())
print(m.capitalize())
print(m.swapcase())

w=' livewire computer center '
print(w)
print(w.strip())
print(w.lstrip())
print(w.rstrip())
'''
#Replace
'''
m="Python Programming"
print(m.replace("P","J"))
print(m.replace("Python","Java"))
'''
#Find
'''
print(m.find("m"))
'''
#Split
'''
a="Python,Programming"
print(a.split(","))
print(a.split("o"))

a="yokeshwaran"
b="senthi"
c="02.06.2007"
d="AVC collge"
age=21

print("my name is",(a))
print("my father name is",(b))
print("my birthday date is",(c))
print("my collge name is",(d))


print(f"My name is {a} and i'm {age} years old")

price=100

print(f"Price of the product is {price:.3f} dollars")
'''
#Input
'''
name=input("Enter Your Name:")
print(name)
age=int(input("Enter Your Age:"))
print(age)
mark=float(input("Enter Your Mark:"))
print(mark)

name=input('Enter Your Name:')
father=input('Enter Your Father Name:')
age=int(input('Enter Your Age:'))
mark=int(input('Enter Your Mark:'))
print(name)
print(father)
print(age)
print(mark)
print(name[-2:].upper())

a=input('Enter Your Name:')
b=input('Emter Your Father Name:')
print(name+fathername)

a=input('Enter Your Fist Name:')
b=input('Enter Your Last Name:')
print(a.strip()+b.strip())

a=input('Enter Your Name:')
b=a.replace(' ','')
print(b)
print(len(b))
'''
#Operators

#Arithmetic Operators
'''
a=10
b=5

print("Add            :",a+b)
print("Subract        :",a-b)
print("Multiply       :",a*b)
print("Divide         :",a/b)
print("Floor Division :",a%b)
print("Exponation     :",a**b)
'
'''
#Assignment Operator
'''
a=10

a+=10#a=a+10
print(a)
a-=10
print(a)
a*=10
print(a)
a/=10
print(a)
'''
#Comparision Operator
'''
a=10
print(a==10)
print(a!=11)
print(a<20)
print(a>10)
print(a>=10)
print(a<10)
print(a<=10)

'''
#Logical Operators
'''
x=10
y=5
print(x==10 and y==5)
print(x==1 or y==5)
print(not(x==1))
'''
#Bitwise Operator
'''
a=6
b=8
print(a&b)
pri nt(a|b)
print(a^b)
print(~a)
print(~b)
a=6
b=8
print(a<<b)
print(a>>b)
'''
#Membership Operator
'''
a=["Hello","Python"]
print("Hello" in a)
b=[1234,5678]
print(1234 in b)

print("Hi" not in a)
a=int(input("Enter a Integer:"))
b=a%100
print(b)
print(b//10)
'''
#Condition Statements
'''
a=10
if(a==1):
    print("A is 10")
elif(a==11):
    print("Else A is 10")
else:
    print("A is not 10")

a=10
b=10
if(a>b):
    print("A is bigger than A")
elif(a<b):
    print("B is bigger than B")
else:
    print("Both are Equal")

a=int(input('a:'))
b=int(input('b:'))
c=int(input('c:'))
print(a)
print(b)
print(c)

if(a>b and a>c):
    print('"A" is bigger than "B or C"')
elif(a<b and b>c):
    print('"B" is bigger than "A or C"')
elif(c>a and c>b):
    print('"C" is bigger than "A or B"')

a=int(input('a:'))
print(a)

if(a>0):
    print('its is positive')
elif(a<0):
    print('its is negative')
else:
    print('its is "0"')

a=int(input('Enter your age:'))
print(a)

if(a>=18 and a<120):
    print("Eligible to Vote")
elif(a<18 and a>0):
    print("Not Eleigible to Vote")
elif(a>120):
    print("Your age is 'Over'")
else:
    print("Negative age is 'not'")'''

'''a=int(input('Enter your Number:'))
print(a)
if(a%2==0):
    print("Even")
else:
    print("odd")'''


'''a=int(input('Enter your Number:'))
print(a)

if(a%11==0 and a%5==0):
    print("its number is '5' and '11' Divide Number")
elif(a%5==0):
    print("its number is only '5' Divide Number")
elif(a%11==0):
    print("its number is only '11' Divide Number")
else:
    print("its number is '5' and '11' not Divide Number")

a,b,c=input('Student Name:'),input('Student Reg No:'),input('Student School Name:')
t,e,m,s,ss=int(input('Tamil Mark:')),int(input('English Mark:')),int(input('maths Mark:')),int(input('Science Mark:')),int(input('Social Science:'))
print(a),print(b),print(c)
tot=t+e+m+s+ss
print(tot)

if(tot>450):
    print('"O"')
elif(tot>400 and tot<=450):
    print('"A"').
    
elif(tot>350 and tot<=400):
    print('"B"')
else:
    print('"C"')


a=int(input('Enter your Number:'))
print(a)
b=a%100
print(b)
print(b//10)
c=(b//10)
print(c+10)



a,b,c=input('Enter your Name:'),int(input('Enter your age:')),input('Enter your places:').lower()

if(b<18 and c!="mayiladuthurai"):
    print("Your not eligible")
elif(b<18):
    print('You must complet "18" to attend the exam')
elif(c!="mayiladuthurai"):
    print('Out of Places')
else:
    print("Your eligible")
'''   
#Nested if
'''
a=1
if(a%2==0):
    print("The Number is divided by 2")
    if(a%4==0):
        print("And also divided by 4")
    else:
        print("The number is only divided by 2 ")
    
else:
    print("The number is not divided by both 2 and 4")

a=input("Did you have a voter id?\na)yes \nb)no\n")

a,b=input('Enter your Name:'),int(input('Enter your age:'))

if(b>=18):
   v=input("Did you have a voter id?\na)yes \nb)no\n").lower()
   
   if(v!="yes"):
      print("Your not Eligible")
   else:
      print('Your Eligible')
else:
    print('You must complet "18"')

a,b=int(input('1 number:')),int(input('2 number:'))
v=input("(a)add \n(b)subract \n(c)multiply \n(d)divide\n:").lower()

if(v=="add"):
    print(a+b)
elif(v=="subract"):
    print(a-b)
elif(v=="multiply"):
    print(a*b)
elif(v=="divide"):
    print(a/b)
#Check the shop is closed or Open
x=int(input('Enter your visting time:'))
y=input("a)am \nb)pm \n").lower()
if(y=='am'):
    if(x==9<11):
        print('shop is open')
    else:
        print('shop is close')
elif(y=='pm'):
    if(x==1<10 or x==12):
        print('shop is open')
    else:
        print('shop is close')
        
else:
   pass
'''
#ATM Withdrawal System
'''
c=10000
a=int(input('Withdrawal Amount:'))
if(a<c):
    if(a%100==0):
        print("Collect your Cash\nBalance:",c-a)
    else:
        print("This ATM can only dispence multiples of 100")

else:
    print("Overlimit\nBalance:",c)'''
#------------------------------------------------------------------------------------------------------------------------------
'''a,b,=input('Student Name:'),int(input('Student age:'))

if(b>=18):
    t,e,m,s,ss=int(input('Tamil Mark:')),int(input('English Mark:')),int(input('maths Mark:')),int(input('Science Mark:')),int(input('Social Science Mark:'))
    if(t>=35 and e>=35 and m>=35 and s>=35 and ss>=35):
        print('Pass')
        if(t+e+m+s+ss):
            print('Mark:')
            print(t+e+m+s+ss)
            tot=t+e+m+s+ss
            if(tot//5):
                print("Average Mark:")
                print(tot//5)
                x=tot//5
                if(x>=90):
                    print('Your Eligible "MBS"')
                elif(x>=80):
                    print('Your Eligible "Engineering"')
                elif(x>=70):
                    print('Your Eligible "Science"')
                elif(x>=60):
                    print('Your Eligible "auto"')
                elif(x>=50):
                    print('Your Eligible "History"')
    else:
        print('Fail')
else:
    print('You must complet "18"')
'''    
#simple for
'''
for x in range(15):
    print("run this time",x)
 ''' 
#loops
'''
for i in range(1,10,3):
    print(i)


for i in range(5):
    if(i==3):
        continue
    print(i)
    
for i in range(10):
    if(i==5):
        break
    print(i)

for x in range(1,101,2):
        print(x)

for y in range(100,0,-1):
    if(y%2==0):
       print(y)

for a in range(1,50):
    if(a%5==0):
        print(a,afor x in range(5): 
    print("*"*x)


for y in range(4,0,-1):
    print('*'*y)

for z in range(4,0,-1):
    print(" "*(5-z)+"*"*z)
-------------------------------------------

a=int(input('Total Student Number:'))
for x in range(a):
   n= input("Student Name:")
   age= input("Student Age:")
   scl= input("Student School Name:")
   print(n,age,scl)
'''
#---------------------------------------------------------------------------------------------------------------------------
'''
c=0
x=input('Enter your World:')
for a in x:
    if(a=='a' or a=='e' or a=='i' or a=='o' or a=='u'):
       print(a)
       c+=1
    else:
        pass
        
print(c)
'''
#loops
'''

for i in range(0,5):
    if(i%2==0):
        print(i)
    else:
        continue

a='python'
for i in a:
    print(a)


a='python'
for i in a:
    print(i)
'''
#factorial
'''
q = int(input('Enter your Number:'))
i=1
for x in range (1,q+1):
    i=i*x
    print(i)
'''
#while
'''
i=1
while(i<=5):
    i+=1
    print(i)
    if(i==3):
       break
       
i=5
while(i>0):
    print(i)
    i-=1
    
i=1
while(i<=99):
    i+=1
    
    if(i%2==0):
       print(i)
       '''
#Password
'''
correct_password = "1234567890"

while True:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Access granted.")
        break
    else:
        print("Incorrect password. Try again.")
'''
#username & password
'''
i=0
correct_username = "user123"ṇ
correct_password = "1234567890"
while(i<3):
     username = input("Enter the username: ")
     password = input("Enter the password: ")
     if username == correct_username:
         if password == correct_password:
             print("Access granted.")
             break
     else:
        print("Incorrect password. Try again.")
        i+=1
  '''      
#Sum numbers until the user types 0
'''
x=0
a = int(input('Enter your Number:'))
while(a!=0):
    x+=a
    a = int(input('Enter your Number:'))
    
print(x) '''   

#Create a multiplication table for a given number
'''
a=int(input('Enter your Number:'))
i=0
while(i<=9):
    i+=1
    print(i,'*',a,'=',i*a)
'''
#Simulate a basic calculator (until user exits)
'''
while True:
    a,b=int(input('1 number:')),int(input('2 number:'))
    v=input("(a)add \n(b)subract \n(c)multiply \n(d)divide\n:")

    if(v=="add"):
        print(a+b)
    elif(v=="subract"):
        print(a-b)
    elif(v=="multiply"):
        print(a*b)
    elif(v=="divide"):
        print(a/b)

    i=input("you retry ?\na)yes \nb)no\n:").lower()
    if(i=="no"):
      break'''
#---------------------------------------------------------------------------------------------------------------------------
'''
x=0
a = int(input('Enter your Number:'))
while(a!=0):
    x+=a
    a = int(input('Enter your Number:'))
    
print(x)'''

#---------------------------------------------------------------------------------------------------------------------------
'''

a=0
b=1
c=0
i=0
while(i<10):
    print(a)
    c=a+b
    a=b
    b=c
    i+=1
    '''

# Amstrong Number---------------------------------------------------------------------------------------------------------------------------
'''i= int(input('Enter your Number:'))
x=(i%100)
a,b,c=(i//100),(x//10),(i%10)
a1,b1,c1=a*a*a,b*b*b,c*c*c
i1=a1+b1+c1
if(i==i1):
    print('Amstrong Number')
else:
    print(' Not Amstrong Number')'''
#-------------------------------------------------------------------------------------------------------------------
'''
i= int(input('Enter your Number:'))
check=i
d=0
a=0
while i>0:
    d=i%10
    a=a+d**3
    i=i//10
print(a)
if(check==a):
    print("Amstrong")
else:
    print("Not an Amstrong")'''
   
#-------------------------------------------------------------------------------------------------------------------
'''
i1= int(input('Enter your Number:'))
i2= int(input('Enter your Number:'))
i3= int(input('Enter your Number:'))

while True:
    if(i1%2==0)and(i2%2==0)and(i3%2==0):
        print('Number:',i1+i2+i3)
        break
    else:
        print('Try again')
        i1= int(input('Enter your Number:'))
        i2= int(input('Enter your Number:'))
        i3= int(input('Enter your Number:'))'''
#-------------------------------------------------------------------------------------------------------------------
'''i= int(input('Enter your Number:'))
i2=i*i
d=0
r=0
while i>0:
    d=i%10
    r=r*10+d
    i=i//10
print(r)
x=r*r
y=0
z=0
while x>0:
    y=x%10
    z=z*10+y
    x=x//10
print(z)
if(i2==z):
    print('yes')
else:
    print('no')i1=i
while

        '''
#Palindrome world---------------------------------------------------------------------------------------------------------
'''
x = input('Enter your World:')
y=x[::-1]
while(x==y):
    print('palindrome world')
    break'''
#Palindrome number---------------------------------------------------------------------------------------------------------
'''i= int(input('Enter your Number:'))
a=i
b=0
c=0
while i>0:
    b=i%10
    c=c*10+b
    i=i//10
printcr)
if(a==c):
    print('palindrome number')
else:
    print('Not palindrome number')'''
'''
#Function
def add():
    print(2+5)
add()
#arguments
def add(a,b):
    print(a+b)
add(7,3)
#Arbiitary function
def arbit(*a):
    print(a[2])
arbit(2,3,4,8,9)'''
#Function test------------------------------------------------------------------------------------------------------------------------------
'''def Amstrong():
    i = int(input('Enter your Number:'))
    x=(i%100)
    a,b,c=(i//100),(x//10),(i%10)
    a1,b1,c1=a*a*a,b*b*b,c*c*c
    i1=a1+b1+c1
    if(i==i1):
        print('Amstrong Number')
    else:
        print(' Not Amstrong Number')
           
def Palindrome():
    i= int(input('Enter your Number:'))
    q=i
    d=0
    r=0
    while i>0:
        d=i%10
        r=r*10+d
        i=i//10
    print(r)
    if(q==r):
        print('palindrome number')
    else:
        print('Not palindrome number')
def fibo():
    a=0
    b=1
    c=0
    i=0
    while(i<10):
        print(a)
        c=a+b
        a=b
        b=c
        i+=1
def factorial():
    q = int(input('Enter your Number:'))
    i=1
    for x in range (1,q+1):
        i=i*x
        print(i)

q = int(input('Enter your Number:'))
if(q==1):
    Amstrong()
elif(q==2):
    Palindrome()
elif(q==3):
    fibo()
elif(q==4):
    factorial()
else:
    print('Not used Number')'''


'''
def mark():
    a,b,=input('Student Name:'),int(input('Student age:'))
    if(b>=18):
        t=int(input('Tamil Mark:'))
        e=int(input('English Mark:'))
        m=int(input('maths Mark:'))
        s=int(input('Science Mark:'))
        ss=int(input('Social Science Mark:'))
        if(t>=35 and e>=35 and m>=35 and s>=35 and ss>=35):
            print('----------------------------------------------------------------------------------------------')
            print('Student Name:',a)
            print('Student age:',b)
            print('Pass')
            if(t+e+m+s+ss):
                print('Mark:',t+e+m+s+ss)
                tot=t+e+m+s+ss
                if(tot//5):
                    print("Average Mark:",tot//5)
                    x=tot//5
                    if(x>=90):
                        print('Your Eligible "MBS"')
                    elif(x>=80):
                        print('Your Eligible "Engineering"')
                    elif(x>=70):
                        print('Your Eligible "Science"')
                    elif(x>=60):
                        print('Your Eligible "auto"')
                    elif(x>=50):
                        print('Your Eligible "History"')
        else:
            print('----------------------------------------------------------------------------------------------')
            print('Student Name:',a)
            print('Student age:',b)
            print('Fail')
    else:
        print('----------------------------------------------------------------------------------------------')
        print('Student Name:',a)
        print('Student age:',b)
        print('You must complet "18"')
mark()'''


























  
