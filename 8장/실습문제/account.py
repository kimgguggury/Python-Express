class BankAccount :
    def __init__(self) :
        self.__balance = 0
    
    def deposit(self, balance) :
        self.__balance += balance
        return self.__balance
    
    def withdraw(self, balance) :
        if self.__balance - balance <0 :
            print("잔액부족")
        else :
            self.__balance -= balance
            print(f"{balance}출금 완료")
            return self.__balance
        

a = BankAccount()
a.deposit(100)
money =a.withdraw(10)
print(f"남은 돈{money}")