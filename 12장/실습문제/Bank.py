class Bank :
    
    def __init__(self) :
        pass
    
    def getInterestRate(self) :
        print("이자율")
    
class BadBank(Bank) :
    def __init__(self) :
        super().__init__()
    
    def getInterestRate(self) :
        print("BadBank 의 이자율 : 10.0")

class NormalBank(Bank) :
    def __init__(self) :
        super().__init__()
    
    def getInterestRate(self) :
        print("NormalBank 의 이자율 : 8.0")

class GoodBank(Bank) :
    def __init__(self) :
        super().__init__()
    
    def getInterestRate(self) :
        print("GoodBank 의 이자율 : 8.0")

Bad = BadBank()
Bad.getInterestRate()


Normal = NormalBank()
Normal.getInterestRate()

Good = GoodBank()
Good.getInterestRate()    