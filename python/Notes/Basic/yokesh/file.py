'''def great():
    correct_username = "user123"
    correct_password = "1234567890"
    while True:
     # Prompt the user for username and password
     username = input("Enter the username: ")
     password = input("Enter the password: ")
     if username == correct_username:
         if password == correct_password:
             print("Access granted.")
             break    
     else:
        print("Incorrect password. Try again.")
        
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
    
def num(a):
    for y in range(a,0,-1):
     print(y)'''


     
def Palindrome():
    i=int(input("Enter a number:"))
    a=i
    c=0
    while i>0:
        c=c*10+i%10
        i=i//10
    print(c,a)    
    if(a==c):
        print('palindrome number')
    else:
        print('Not palindrome number')


















