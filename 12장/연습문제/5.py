class Animal :
    def __init__(self, age) :
        self.age = age
    
    def eat(self) :
        print("동물이 먹고 있습니다.")
    

class Cat(Animal) :
    def __init__(self, name, age, breed) :
        super().__init__(age)
        self.name = name
        self.breed = breed

def get_oldest_cat(*args) :
    maxAge = max(args)
    return maxAge
    
c1 = Cat("쩔미",3,3)
c2 = Cat("바보",4,3)
c3 = Cat("ㅠㅠ",5,3)


print("가장 나이가 많은 고양이는"+str(get_oldest_cat(c1.age, c2.age, c3.age))+"입니다.")