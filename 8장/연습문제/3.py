class Box :
    
    def __init__(self, l, h, d) :
        self.__l = l
        self.__h = h
        self.__d = d
        
    def __str__(self) :
        msg = "("+str(self.__l)+","+str(self.__h)+","+str(self.__d)+")"
        return msg
    
    def setLength(self, l) :
        self.__l = l
    
    def setHeight(self, h) :
        self.__h = h
    
    def setDepth(self, d) :
        self.__d = d
    
    def getLength(self, l) :
        return self.__l
    
    def getHeight(self, h) :
        return self.__h 
    
    def getDepth(self, d) :
        return self.__d

b1 = Box(100, 100, 100)
print(b1)
print("상자의 부피는",b1.getDepth()*b1.getHeight()*b1.getLength())