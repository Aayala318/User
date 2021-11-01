# Create a file with the User class, including the __init__ and make_deposit methods
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = 0

    def makeDeposit(self, amount):
        self.account += amount

# Add a make_withdrawal method to the User class
    def makeWithdrawl(self, amount):
        self.account -= amount

# Add a display_user_balance method to the User class
    def displayUserBalance(self):
        print(f'User: {self.name}, Balance: ${self.account}')
    
    def transferMoney(self, otherUser, amount):
        otherUser.makeDeposit(amount)
        self.makeWithdrawl(amount)
        print('\n')

# Create 3 instances of the User class
# Have the first user make 3 deposits and 1 withdrawal and then display their balance
denisse = User('Denisse', 'djlove@1.com')
denisse.makeDeposit(10)
denisse.makeDeposit(5)
denisse.makeDeposit(2)
denisse.makeWithdrawl(3)
denisse.displayUserBalance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
jojo = User('Jojo', 'jham@23.com')
jojo.makeDeposit(20)
jojo.makeDeposit(30)
jojo.makeWithdrawl(10)
jojo.makeWithdrawl(40)
jojo.displayUserBalance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance
abby = User('Abby', 'abby@ham.com')
abby.makeDeposit(300)
abby.makeWithdrawl(15)
abby.makeWithdrawl(50)
abby.makeWithdrawl(150)
abby.displayUserBalance()

# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
abby.transferMoney(jojo,20)
abby.displayUserBalance()
jojo.displayUserBalance()