#We define the class with the information required for the bank account.
class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    def adjust_interest_rate(self, new_rate):
        #We adjust the new interest rate.
        self.interest_rate = new_rate
        print(f"Interest rate adjusted to {self.interest_rate}%")

    def deposit(self, amount):
        #Amount of money to deposit into the account.
        self.amount += amount
        print(f"Deposited ${amount}. New balance: ${self.amount}")

    def withdraw(self, amount):
        #In case there is a money withdrawal.
        if amount <= self.amount:
            self.amount -= amount
            print(f"Withdrew ${amount}. New balance: ${self.amount}")
        else:
            #Make sure there is enough founds.
            print("Insufficient funds for withdrawal.")

    def calculate_interest(self, days):
       #Make the calculation of the interest depending on the days.
        interest = (self.amount * self.interest_rate * days) / (365 * 100)
        return interest

    def get_balance(self):
        #Function to request the amount of money that is into the account.
        return self.amount

    def __str__(self):
       #Now the information is going to be introduced in the form of a string.
        return f"Account Holder: {self.name}\nAccount Number: {self.account_number}\nBalance: ${self.amount}\nInterest Rate: {self.interest_rate}%"


def test_bank_account():
    # Creating a BankAcct test.
    acct1 = BankAcct("John Wick", "34215678", 1500.0, 4.5)
    print(acct1)

    # Let's test the deposit.
    acct1.deposit(500.0)

    # Let's try to withdraw money.
    acct1.withdraw(200.0)

    # Now adjust the interest rate.
    acct1.adjust_interest_rate(4.0)

    # Test the interest in 30 days.
    interest = acct1.calculate_interest(30)
    print(f"Interest for 30 days: ${interest:.2f}")

    # Print the bank account information
    print(acct1)


# Finishing, we run the test function. Longest I've done.
test_bank_account()

