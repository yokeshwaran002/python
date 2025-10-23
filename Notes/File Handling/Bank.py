#open("Bank.txt","x")

Bank=open("Bank.txt","a")
Bank.write("Account Number\tBalance\n")
Bank.close()'''
#register

Bank=open("Bank.txt","a")
Account_Number=int(input("Enter the Account Number:"))
Balance=int(input("Enter the Balance:"))
Bank.write(str(Account_Number)+"\t"+str(Balance)+"\n")
Bank.close()'''
#login

Account_Number=int(input("Enter the Account Number:"))
Bank=open("Bank.txt","r")
for line in Bank:
    if line.split("\t")[0]==str(Account_Number):
        print("Account Number is correct")
        Balance=int(line.split("\t")[1])
        print("Your Balance is:", Balance)
        Bank.close()
        break
else:
        print("Account Number not found")

Bank.close()
#withdraw

Account_Number=int(input("Enter the Account Number:"))
Bank=open("Bank.txt","r")
for line in Bank:
    if line.split("\t")[0]==str(Account_Number):
        print("Account Number is correct")
        Bank.close()
        Balance=int(line.split("\t")[1])
        print("Your Balance is:", Balance)
        withdraw=int(input("Enter the amount to withdraw:"))
        if withdraw>Balance:
            print("Insufficient Balance")
        else:
            Balance-=withdraw
            print("Your balance is:", Balance)
        break
else:
        print("Account Number not found")
Bank=open("Bank.txt","w")
Bank.write("Account Number\tBalance\n")
Bank.write(str(Account_Number)+"\t"+str(Balance)+"\n")
Bank.close()
#deposit

Account_Number=int(input("Enter the Account Number:"))
Bank=open("Bank.txt","r")
for line in Bank:
    if line.split("\t")[0]==str(Account_Number):
        print("Account Number is correct")
        Bank.close()
        Balance=int(line.split("\t")[1])
        print("Your Balance is:", Balance)
        deposit=int(input("Enter the amount to deposit:"))
        Balance+=deposit
        print("Your balance is:", Balance)
        break
else:
        print("Account Number not found")
Bank=open("Bank.txt","w")
Bank.write("Account Number\tBalance\n")
Bank.write(str(Account_Number)+"\t"+str(Balance)+"\n")
Bank.close()







