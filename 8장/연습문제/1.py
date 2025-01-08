class Cat :
    def __init__ (self, name = "", age = 0):
        self.name = name
        self.age = age
    
    def __str__(self) :
        msg = "고양이의 이름 : " + self.name +  " 고양이의 나이 " + str(self.age)
        return msg
    
    def setName(self, name) :
        self.name = name
    
    def setAge(self, age) :
        self.age = age
    
    def getName(self, name) :
        return self.name
    
    def getAge(self, age) :
        return self.age

missy = Cat("Missy", 3)
lucky = Cat("Lucky", 5)
print(missy)
print(lucky)