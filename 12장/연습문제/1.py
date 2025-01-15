class Point :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    
    def __str__(self) :
        return '(%d, %d)' % (self.x, self.y)


class Point3D(Point) :
    def __init__(self,x, y, z = 0) :
        super().__init__(x,y)
        self.z = z
    
    def __str__(self) :
        return '(%d, %d, %d)' % (self.x, self.y, self.z)

D2 = Point(1, 1)
D3 = Point3D(1,1,1)

print(D2)
print(D3)