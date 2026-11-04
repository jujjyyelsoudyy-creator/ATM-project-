from time import sleep 
accounts = {"jana" : 2000 ,
            "eyad" : 4000 ,
            "ehab" : 1000 }
#withdraw function 
def withdraw(user) : 
    if user in accounts.keys() : 
        amount = float(input("Enter the amount to withdraw :"))
        if amount <= accounts[user] :
            accounts[user] -= amount
            sleep(1)
            print("successful withdraw")
            print("remaning balance",accounts[user])
        else :
            print("not enough")
    else :
        print("user not found")  
#withdraw(input("Enter the user :"))
#deposit function
def deposit (user) :
    if user in accounts.keys() :
        amount = float(input("Enter the amount to deposit :"))
        if amount >0 :
            accounts [user] += amount
            sleep(1)
            print("Deposit successful")
            print("remaning balance",accounts[user])
        else :
            print("invalid amount")
    else :
        print("user not found")
#deposit(input("Enter the user :"))
#transfer function 
def transfer(sender) :
    receiver = input("Enter account name to transfer :")
    if receiver in accounts :
        amount = float(input("Enter amount to transfer :"))
        if accounts[sender]>=amount : 
            accounts[sender]-=amount
            accounts[receiver]+=amount
            print("Transfer done successfully")
            print("Remaning balance :",accounts[sender])
        else :
            print("your  balance not enough")
    else :
        print("Receiver not found")
user = input("Enter the user :")

if user in accounts :
        print("1.withdraw")
        print("2.deposit")
        print("3.Transfer")

        choose = input("choose your opeartion 1 or 2 or 3 :")
        if choose == "1" :
            withdraw(user)
        elif choose == "2":
            deposit(user)
        elif choose == "3" :
            transfer(user) 
        else :
            print("invalid choose")

else :
    print("user not found")
