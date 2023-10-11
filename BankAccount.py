from Validate import *

class BankAccount:
    def __init__(self, bname, ifsc, accNum, name, age, gender, dob, address, city, accType, balance, pan, aadhaar):
        self.bname = bname
        self.ifsc = ifsc
        self.accNum = accNum
        self.name = name
        self.age = age
        self.gender = gender
        self.dob = dob
        self.address = address
        self.city = city
        self.accType = accType
        self.balance = balance
        self.pan = pan
        self.aadhaar = aadhaar
        self.transactions = []

    def display(self):
        print(f"Bank Name - {self.bname}\n"
              f"IFSC code - {self.ifsc}\n"
              f"Account Num - {self.accNum}\n"
              f"Name - {self.name}\n"
              f"Age - {self.age}\n"
              f"Gender - {self.gender}\n"
              f"DOB - {self.dob}\n"
              f"Address - {self.address}\n"
              f"City - {self.city}\n"
              f"Account Type - {self.accType}\n"
              f"Balance - {self.balance}\n"
              f"Pan - {self.pan}\n"
              f"Aadhaar - {self.aadhaar}\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            transaction_description = f"Deposited Rs {amount}"
            self.add_transaction(transaction_description)
            return f"Deposited Rs {amount}. New balance: Rs {self.balance}"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            transaction_description = f"Withdrew Rs {amount}"
            self.add_transaction(transaction_description)
            return f"Withdrew Rs {amount}. New Balance: Rs {self.balance}"
        else:
            return "Insufficient balance or invalid withdrawal amount."

    def transferFunds(self, receiver_account, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            receiver_account.balance += amount
            transaction_description = f"Transferred Rs {amount} to {receiver_account.name}"
            self.add_transaction(transaction_description)
            return f"Transferred Rs {amount} to {receiver_account.name}"
        else:
            return "Insufficient Funds or invalid transfer amount"

    def add_transaction(self,transaction_description):
        self.transactions.append(transaction_description)

    def generate_statement(self):
        statement = f"Account statement for {self.name} (Account Number: {self.accNum}):\n"
        for i, transaction in enumerate(self.transactions,start=1):
            statement += f"{i}. {transaction}\n"
        return statement


bank_accounts = {}


# ---------------- CREATE ACCOUNT ------------------------

def createAccount():
    while True:
        bname = input("Enter Bank Name (HDFC/AXIS/SBI/KOTAK)- ").upper()
        if validate_bname(bname):
            break
        else:
            print("Invalid Bank Name !!! Please choose from the given options ")


    while True:
        accNum = input("Enter Account Number - ")
        if validate_AccNum(accNum):
            if accNum not in bank_accounts.keys():
                break
            else:
                print("Account Number already exists. Re-enter Account number")
        else:
            print("Invalid Account Number !!! It should range between 8 to 14 digits ")

    while True:
        ifsc = input("Enter IFSC Code (ABCD0123456)- ").upper()
        if validate_IFSC(ifsc):
            break
        else:
            print("Invalid IFSC !!! Please Enter it again ")

    while True:
        name = input("Enter Account Holder Name - ").title()
        if validate_name(name):
            break
        else:
            print("Invalid name")

    while True:
        dob = input("Enter Date of Birth (dd-mm-yyyy) - ")
        if validate_date(dob):
            break
        else:
            print("Invalid Date pattern !!! Please refer the given pattern ")

    current_date=datetime.now()
    dob1 = datetime.strptime(dob,"%d-%m-%Y")
    age = current_date.year - dob1.year - ((current_date.month,current_date.day) < (dob1.month, dob1.day))

    while True:
        gender = input("Enter Gender (Male/Female/Others) - ").title()
        if validate_gender(gender):
            break
        else:
            print("Invalid Gender !!! Please choose from the given options ")


    address = input("Enter Address - ").title()
    city = input("Enter City - ").title()

    while True:
        accType = input("Enter Account Type (Savings/Salary/Joint) - ").title()
        if validate_accType(accType):
            break
        else:
            print("Invalid Account Type !!! Please choose from the given options ")

    balance = 0

    while True:
        pan = input("Enter PAN card number - ").upper()
        if validate_pancard(pan):
            break
        else:
            print("Invalid PAN number !!! Please enter it again ")

    while True:
        aadhaar = input("Enter AADHAAR card number - ")
        if validate_aadhaar(aadhaar):
            break
        else:
            print("Invalid Aadhaar Number !!! Please enter 12 digit aadhaar number ")

    account = BankAccount(bname, ifsc, accNum, name, age, gender, dob, address, city, accType, balance, pan, aadhaar)
    bank_accounts[accNum] = account
    print(" ")
    print("Account created successfully !")


# ---------- UPDATE ACCOUNT ---------

def updateAccount():
    account_number = input("Enter Account number to update - ")
    if account_number in bank_accounts.keys():
        print("Select option to update - ")
        print("Enter 1 - Update NAME ")
        print("Enter 3 - Update ADDRESS ")
        print("Enter 3 - Update DOB ")
        print("")
        option = input("enter your choice: ")

        if option == "1":
            new_name = input("Enter new name: ").title()
            if validate_name(new_name):
                bank_accounts[account_number].name = new_name
            else:
                print("Invalid name")

        elif option == "2":
            new_address = input("Enter new address: ").title()
            bank_accounts[account_number].address = new_address

        elif option == "3":
            new_dob = input("Enter new DOB (dd-mm-yyyy): ")
            if validate_date(new_dob):
                bank_accounts[account_number].dob = new_dob
            else:
                print("Invalid Date pattern !!! Please refer the given pattern ")

        else:
            print("Invalid option")
    else:
        print("Account not found. Enter correct Account Number")


# ------- DEPOSIT MONEY ---------

def deposit():
    account_number = input("Enter Account number to deposit money into - ")
    if account_number in bank_accounts.keys():
        amount = float(input("Enter deposit amount: "))
        print(bank_accounts[account_number].deposit(amount))
    else:
        print("Account not found. Enter correct Account Number")


# ------- WITHDRAW MONEY ---------

def withdraw():
    account_number = input("Enter Account number to withdraw money from - ")
    if account_number in bank_accounts.keys():
        amount = float(input("Enter withdrawal amount: "))
        print(bank_accounts[account_number].withdraw(amount))
    else:
        print("Account not found. Enter correct Account Number")


# ------- TRANSFER FUNDS ---------

def transferFunds():
    sender_accNum = input("Enter the sender's account number - ")
    receiver_accNum = input("Enter the receiver's account number - ")

    if sender_accNum in bank_accounts.keys() and receiver_accNum in bank_accounts:
        amount = float(input("Enter the amount to be transferred:  "))
        print(bank_accounts[sender_accNum].transferFunds(bank_accounts[receiver_accNum], amount))
    else:
        print("One or both accounts not found")


# ------- SEARCH DETAILS ---------

def searchDetails():
    print("Select search option ")
    print(" Enter 1: Search by Account Number")
    print(" Enter 2: Search by Name")
    print(" Enter 3: Search by Type of Account (Savings/Salary/Joint)")

    option = input("Enter your choice ")

    if option == "1":
        acc_num = input("Enter account number to search: ")
        if acc_num in bank_accounts.keys():
            bank_accounts[acc_num].display()
        else:
            print("Account not found.")

    elif option == "2":
        found = False
        sname = input("Enter name to search: ").title()
        for acc_num, account in bank_accounts.items():
            if account.name == sname:
                account.display()
                found = True
        if not found:
            print("Account not found for the given name")

    elif option == "3":
        account_type = input("Enter type of account to search: ").title()
        found = False
        for acc_num, account in bank_accounts.items():
            if account.accType == account_type:
                account.display()
                found = True
        if not found:
            print("Account not found for the specified account type")

    else:
        print("Invalid Option")

# ------- CHECK BALANCE ---------

def checkBalance():
    account_number = input("enter the account number for which you want to check balance - ")
    if account_number in bank_accounts.keys():
        print(bank_accounts[account_number].balance)
    else:
        print("Account not found")

# ------- DELETE ACCOUNT ---------

def deleteAccount():
    account_number = input("enter the account number to delete - ")
    if account_number in bank_accounts:
        del bank_accounts[account_number]
        print("Account Deleted successfully!")
    else:
        print("account not found")


def generateStatement():
    account_number = input("enter the account number you want to generate the statement for - ")
    if account_number in bank_accounts.keys():
        account = bank_accounts[account_number]
        statement = account.generate_statement()
        print(statement)
    else:
        print("Account not found.")


# ----------- MAIN MENU LOOP ---------------

while True:
    print(" ")
    print("1: Press 1 to Create Account ")
    print("2: Press 2 to Display Records ")
    print("3: Press 3 to update Account Details ")
    print("4: Press 4 to Deposit money ")
    print("5: Press 5 to Withdraw money ")
    print("6: Press 6 to Transfer funds ")
    print("7: Press 7 to Search Details of Account Holder ")
    print("8: Press 8 to Check Balance ")
    print("9: Press 9 to Delete Account ")
    print("10: Press 10 to Generate Statement ")
    print("11: Press 11 to exit ")
    print(" ")
    choice = int(input("Enter your choice - "))

    if choice == 1:
        createAccount()

    elif choice == 2:
        for i in bank_accounts.values():
            i.display()

    elif choice == 3:
        updateAccount()

    elif choice == 4:
        deposit()

    elif choice == 5:
        withdraw()

    elif choice == 6:
        transferFunds()

    elif choice == 7:
        searchDetails()

    elif choice == 8:
        checkBalance()

    elif choice == 9:
        deleteAccount()

    elif choice == 10:
        generateStatement()

    elif choice == 11:
        print("Exiting the Banking Management System")
        break

    else:
        print("Invalid Choice, please select a valid option")
