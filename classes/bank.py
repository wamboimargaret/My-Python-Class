class Account:
    bank_name = "ABSA"
    def __init__(self, account_name, account_no, balance, loan_balance, deposits, withdwrals):
        self.account_name = account_name
        self.account_no = account_no
        self.balance = balance
        self.loan_balance = 0
        self.deposits = []
        self.withdrawals = []

    def deposit(self, amount):
        self.balance+= amount
        withdrawal_transaction = {"amount": amount, "narration": "deposit"}
        self.deposits.append(withdrawal_transaction)
        return f"{self.account_name} has deposited {amount}, the balance is {self.balance}."
    
    def withdraw(self, amount):
        if amount >= self.balance:
            self.balance -= amount
            withdrawal_transaction = {"amount": amount, "narration": "withdrawal"}
            self.withdrawals.append(withdrawal_transaction)
        
            return f"{self.account_name} has withdrawn {amount}, the balance is {self.balance}."
        else: 
            return f" Hello {self.account_name}, your balance: {self.balance} please enter a lower amount."
    
    def display_account_details(self):
        return f"{self.account_no}, {self.account_name}, {self.balance}"
    
    def check_balance(self):
        return f"Hello, {self.account_name} your balance for account{self.account_no} is {self.balance}."
    
    def print_statement(self):
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
            print(f"{transaction['narration']} - {transaction['amount']}")

            
    def borrow_loan(self, amount):
        if self.loan_balance > 0:
            return "You already have an outstanding loan"
        elif amount <= 100:
            return "Loan amount must be greater than 100"
        elif len(self.deposits) < 10:
            return "You must have made at least 10 deposits to be eligible for a loan"
        elif amount > sum([deposit['amount'] for deposit in self.deposits])/3:
            return "Loan amount requested is more than 1/3 of your total deposits"
        else:
            self.loan_balance += amount
            return f"Your loan of ${amount} was successful. Your new loan balance is ${self.loan_balance}"
    def repay_loan(self, amount):
        if amount > self.loan_balance:
            self.balance += amount - self.loan_balance
            self.loan_balance = 0
            return f"You have successfully repaid your loan. Your new balance is ${self.balance}"
        else:
            self.loan_balance -= amount
            return f"You have successfully repaid ${amount} of your loan. Your new loan balance is ${self.loan_balance}"
    def transfer(self, amount, account):
        if amount > self.balance:
            return f"Insufficient funds. Your current balance is ${self.balance}"
        else:
            self.balance -= amount
            account.deposit(amount)
            return f"You have successfully transferred ${amount} to account {account.account_number}. Your new balance is ${self.balance}"