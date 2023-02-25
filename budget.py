
class Category:
    def __init__(self, name):
        """
        Initialize the Category class with a name.
        """
        self.name = name
        self.ledger = []
        print("Category class initialized with name:", self.name)

def deposit(self, amount, description=""):
        """
        Method to add a deposit to the ledger.
        """
        self.ledger.append({"amount": amount, "description": description})
        print("Deposit of", amount, "added to ledger")
    
def withdraw(self, amount, description=""):
        """
        Method to add a withdrawal to the ledger.
        """
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            print("Withdrawal of", amount, "added to ledger")
            return True
        else:
            return False
    
def get_balance(self):
        """
        Method to calculate and return the balance in the ledger.
        """
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        print("Balance in ledger is:", balance)
        return balance
    
def transfer(self, amount, category):
        """
        Method to transfer money from one budget category to another.
        """
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            print("Transfer of", amount, "from", self.name, "to", category.name, "complete")
            return True
        else:
            return False
    
def check_funds(self, amount):
        """
        Method to check if the budget category has enough funds for the requested withdrawal/transfer.
        """
        if self.get_balance() < amount:
            print("Insufficient funds for requested withdrawal/transfer")
            return False
        else:
            print("Sufficient funds for requested withdrawal/transfer")
            return True
    
def __str__(self):
        """
        Method to display the category name, ledger items, and balance when printing the budget object.
        """
        title = f"{self.name}".center(30, "*")
        ledger_items = ""
        for item in self.ledger:
            ledger_items += f"{item['description'][0:23]:<23}{item['amount']:>7.2f}\n"
        balance = f"Total: {self.get_balance():>7.2f}"
        print("Printing budget object...")
        return title + "\n" + ledger_items + balance

def create_spend_chart(categories):
    """
    Function to generate a bar chart of the percentage spent in each budget category.
    """
    chart = "Percentage spent by category\n100|"
    for i in range(10, -1, -10):
        chart += "\n " + str(i) + "|"
        for category in categories:
            if category.get_balance() == 0:
                percentage_spent = 0
            else:
                total_spent = 0
                for item in category.ledger:
                    if item["amount"] < 0:
                        total_spent += -item["amount"]
                percentage_spent = total_spent / category.get_balance() * 100
            if percentage_spent >= i:
                chart += " o"
            else:
                chart += "  "
    chart += "\n    ----------\n     "
    for category in categories:
        chart += category.name[0] + "  "
    chart += "\n     "
    for category in categories:
        chart += category.name[1] + "  "
    chart += "\n     "
    for category in categories:
        if len(category.name) > 2:
            chart += category.name[2] + "  "
        else:
            chart += "   "
    chart += "\n     "
    for category in categories:
        if len(category.name) > 3:
            chart += category.name[3] + "  "
        else:
            chart += "   "
    chart += "\n        "
    for category in categories:
        if len(category.name) > 4:
            chart += category.name[4] + "  "
        else:
            chart += "   "
    chart += "\n        "
    for category in categories:
        if len(category.name) > 5:
            chart += category.name[5] + "  "
        else:
            chart += "   "
    chart += "\n        "
    for category in categories:
        if len(category.name) > 6:
            chart += category.name[6] + "  "
        else:
            chart += "   "
    chart += "\n        "
    for category in categories:
        if len(category.name) > 7:
            chart += category.name[7] + "  "
        else:
            chart += "   "
    return chart

