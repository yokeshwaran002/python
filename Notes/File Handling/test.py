Account_Number = int(input("Enter the Account Number: "))
deposit_amount = int(input("Enter the amount to deposit: "))

with open("Bank.txt", "r") as Bank:
    lines = Bank.readlines()

header = lines[0]
accounts = lines[1:]
updated = False

with open("Bank.txt", "w") as Bank:
    Bank.write(header)
    for line in accounts:
        acc_num, balance = line.strip().split("\t")
        if acc_num == str(Account_Number):
            print("Account Number is correct")
            Balance = int(balance) + deposit_amount
            print("Your new balance is:", Balance)
            Bank.write(f"{acc_num}\t{Balance}\n")
            updated = True
        else:
            Bank.write(line)
    if not updated:
        print("Account Number not found")