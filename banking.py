from datetime import date

class Account:
    acc_number = 0  # class variable

    @classmethod
    def get_account_num(cls):
        Account.acc_number += 1
        return Account.acc_number

    def __init__(self, name, balance, ph_num, pin):
        self.acc_num = Account.get_account_num()
        self.name = name
        self.balance = balance
        self.ph_num = ph_num
        self.pin = pin

class Account_Operations:

    def __init__(self):
        pass

    def create_account(self, accounts):
        name = input('Enter your name: ')
        balance = float(input('Enter your initial Balance: '))
        ph_num = int(input('Enter your Phone number: '))
        pin = int(input('Enter your secret number(4 digits only): '))
        account = Account(name, balance, ph_num, pin)  # Creation of object
        return account

    def is_account_exist(self, accounts, acc_num):
        index = -1
        for i in range(len(accounts)):
            if accounts[i].acc_num == acc_num:
                index = i
                break  # break the loop
        if index == -1:
            print(f'Account with Acc_Number:{acc_num} does not exist')
        return index

    def modify_account(self, accounts, acc_num, pin, ph_num):
        index = self.is_account_exist(accounts, acc_num)
        if index != -1:
            accounts[index].pin = pin
            accounts[index].ph_num = ph_num
            print('Your Account is updated successfully')

    def delete_account(self, accounts, acc_num):
        index = self.is_account_exist(accounts, acc_num)
        if index != -1:
            print(f'Your Account, Acc_Num:{accounts[index].acc_num} is deleted')
            del accounts[index]

    def display_all_accounts(self, accounts):
        if len(accounts) == 0:
            print('No active accounts found')
        else:
            print('All the active accounts are:')
            for account in accounts:
                print(f'Acc_num: {account.acc_num}', end=', ')
                print(f'Name   : {account.name}', end=', ')
                print(f'Balance: {account.balance}', end=', ')
                print(f'Phone Num: {account.ph_num} \n')

    def display_account_details(self, accounts, acc_num):
        index = self.is_account_exist(accounts, acc_num)
        if index != -1:
            print(f'Acc_num: {accounts[index].acc_num}',end = ', ')
            print(f'Name   : {accounts[index].name}', end = ', ')
            print(f'Balance: {accounts[index].balance}')


class Transaction:
    t_id = 505050500

    @classmethod
    def generate_transaction_id(cls):
        Transaction.t_id += 1
        return Transaction.t_id

    def __init__(self, acc_num, type, ):
        self.id = Transaction.generate_transaction_id()
        self.acc_num = acc_num
        self.date =  date.today()
        self.type = type
        self.amount = 0.0

    def set_transaction_amount(self, amount):
        self.amount = amount

class Transaction_Operations:

    def deposit(self, account, amount):
        account.balance += amount
        print(f'Rs.{amount} deposited successfully. Your Current Balance is {account.balance}')
        return account

    def withdraw(self, account, amount):
        account.balance -= amount
        print(f'Rs.{amount} withdrawn successfully. Your Current Balance is {account.balance}')

    def mini_statement(self, account, transactions):
        print('Your last 3 transactions are:')
        count = 0
        for t in transactions:
            if t.acc_num == account.acc_num:
                count += 1
        if count == 0:
            print('You have no transactions in your Account')
            return

        print('%-15s %-10s %5s %-8s' % ('Transaction-ID', 'Date', 'Type', 'Amount'))
        for t in transactions:
            if t.acc_num == account.acc_num:
                print('%-15d %-10s %-5d %6.2f'%(t.id, t.date, t.type, t.amount))
                count += 1
            if count == 3:
                break

    def check_balance(self, account):
        print(f'Your Account Balance is {account.balance}')


def validate_account(accounts):
    oprs = Account_Operations()
    acc_num = int(input('Enter your account number: '))
    index = oprs.is_account_exist(accounts, acc_num)
    if index == -1:
        pass
    else:
        pin = int(input('Enter your pin: '))
        if accounts[index].pin != pin:
            print('InCorrect PIN entered')
            index = -1
    return index

def do_transactions(accounts, transactions):
    print('\"BANKING  TRANSACTIONS \"')
    index = validate_account(accounts)
    if index == -1:
        return
    transact = Transaction_Operations()
    account = accounts[index]

    choice = int(input('1:Deposit 2:Withdraw 3:CheckBalance 4:MiniStmt. 5:Exit Your Choice: '))
    transaction = Transaction(accounts[index].acc_num, choice)
    if choice == 1:
        amount = float(input('Enter the amount to be deposited: '))
        account = transact.deposit(account, amount)
        transaction.set_transaction_amount(amount)
    elif choice == 2:
        amount = float(input('Enter the amount to be withdrawn: '))
        if account.balance < amount:
            print('Insufficient funds in your account')
            return
        transact.withdraw(account, amount) #DOUBTFUL
        transaction.set_transaction_amount(amount)
    elif choice == 3:
        transact.check_balance(account)
    elif choice == 4:
        transact.mini_statement(account, transactions)
    elif choice == 5:
        return choice
    else:
        print('Invalid choice entered')
    transactions.append(transaction)


def account_menu(accounts):
    oprs = Account_Operations()
    account_choice = 0
    while True:
        print('1:Create 2:Modify 3:DisplayOne 4:DisplayAll 5:Delete 6:Exit')
        account_choice = int(input('Your choice: '))
        if account_choice == 1:
            accounts.append(oprs.create_account(accounts))

        elif account_choice == 2:
            acc_num = int(input('Enter your account number: '))
            pin = int(input('Enter your new pin: '))
            ph_num = int(input('Enter your new phone number: '))
            oprs.modify_account(accounts, acc_num, pin, ph_num)

        elif account_choice == 3:
            acc_num = int(input('Enter your account number: '))
            oprs.display_account_details(accounts, acc_num)

        elif account_choice == 4:
            oprs.display_all_accounts(accounts)

        elif account_choice == 5:
            acc_num = int(input('Enter your account number: '))
            oprs.delete_account(accounts, acc_num)

        elif account_choice == 6:
            break  # break the while loop

        else:
            print('Invalid choice entered')


accounts = []
transactions = []
choice = 0

print('Welcome to the most Trusted Bank SBI')
print('\"ACCOUNT  RELATED  BANKING\"')
account_menu(accounts)
while True:
    choice = do_transactions(accounts, transactions)
    if choice == 5:
        break
print('Thank you for banking with us!!!')

'''
    choice = input('Do you wish to exit? Press Y for Yes')
    if choice == 'Y' or choice == 'Y':
        break

'''