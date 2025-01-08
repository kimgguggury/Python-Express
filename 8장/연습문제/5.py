class Triangle :
    
    def __init__ (self, a1, a2, a3) :
        self.__a1 = a1 
        self.__a2 = a2
        self.__a3 = a3
        self.__numberOfSides = 3
    
    def checkAngles(self) :
        if self.__a1 + self.__a2 + self.__a3 == 180 :
            return True
        else :
            return False

triangle = Triangle(90, 30, 60) 
print(triangle.checkAngles())