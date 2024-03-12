import math

class Category:
    def __init__(self, category):
        self.ledger = []
        self.category = category
        self.balance = 0.0
      
    def __str__(self):
        head = self.category.center(30, '*') + '\n'
        body = ''
        for transaction in self.ledger:
            body += f"{transaction['description'][:23]:23}{float(transaction['amount']):7.2f}\n"
        body += f'Total: {self.balance}'
        return head + body
        
        
    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount
        #print(self.balance)

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
          self.ledger.append({"amount": -1 * amount, "description": description}) 
          self.balance -= amount
          #print(self.balance)
          return True
        return False
        
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, toCategory):
        if self.withdraw(amount, description=f'Transfer to {toCategory.category}'):
            toCategory.deposit(amount, description=f'Transfer from {self.category}')
            return True
        return False
    
    def check_funds(self, amount):
        return True if self.balance - amount >= 0 else False
            

def create_spend_chart(categories):
    spend_by_amount = {}
    for category in categories: 
        spent = 0.0  
        for transaction in category.ledger:
            if transaction['amount'] < 0:
                spent -= transaction['amount']

        spend_by_amount.update({f'{category.category}': float("{:.2f}".format(spent))})

    everything_spent = sum(spend_by_amount.values())
    spend_by_percent = {}
    for key, value in spend_by_amount.items():
        number = value/everything_spent*100
        spend_by_percent[key] = int(number // 10 * 10)

    rtn = "Percentage spent by category"

    for i in range(100, -1, -10):
        rtn += "\n" + str(i).rjust(3) + "|"
        for key, value in spend_by_percent.items():
            if value >= i:
                rtn += " o " 
            else:
                rtn+= '   '
        rtn += ' '
    rtn += "\n    ----------"

    categories_length = [len(i) for i in spend_by_percent.keys()]
    max_length = max(categories_length)

    for i in range(max_length):
        rtn += "\n    "
        for j in range(len(categories)):
            if i < categories_length[j]:
                rtn += " " + categories[j].category[i] + " "
            else:
                rtn += "   "
        # Spaces
        rtn += " "

    print(spend_by_amount)
    print(spend_by_percent)
    return rtn