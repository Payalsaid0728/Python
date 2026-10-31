class bankaccount:
    def __init__(self,balance):
        self.__balance = balance
    def show_balance(self):
          return self.__balance
    def deposit(self,balance):
          self.__balance  += balance
          
c1 = bankaccount(5000)
print(c1.show_balance())
c1.deposit(7000)
print(c1.show_balance())