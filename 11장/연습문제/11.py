# class Circle :
#     def __init__(self, radius) :
#         self.__radius = radius
    
#     def __add__(self, other) :
#         self.__radius + other.getRadius()
    
#     def getRadius(self) :
#         return self.__radius

#     def __gt__(self, other) :
#         return self.__radius > other.getRadius()
    
#     def __lt__(self, other) :
#         return self.__radius < other.getRadius()

# c1 = Circle(10)
# c2 = Circle(2)

# print(c1<c2)

import math
 
class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def setRadius(self, radius):
        self.__radius = radius
 
    def getRadius(self):
        return self.__radius
 
    def area(self):
        return math.pi * self.__radius ** 2
 
    def __add__(self, another_circle):
        return Circle( self.__radius + another_circle.__radius )
 
    def __gt__(self, another_circle):
        return self.__radius > another_circle.__radius
 
    def __lt__(self, another_circle):
        return self.__radius < another_circle.__radius
 
    def __str__(self):
        return " 원의반지름: " + str(self.__radius)
 
c1 = Circle(4)
print(c1.getRadius())
 
c2 = Circle(5)
print(c2.getRadius())
 
c3 = c1 + c2
print(c3.getRadius())
 
print( c3 > c2) 
print( c1 < c2) 
 
print(c3)