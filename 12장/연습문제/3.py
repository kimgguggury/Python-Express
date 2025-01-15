import cmath

class Function :
    def __init__(self) :
        pass
    def value(self, x) :
        pass

class Quadratic(Function) :
    def __init__ (self, a, b, c) :
        self.a = a
        self.b = b
        self.c = c
    
    def value(self, x) :
        return (self.a)*x**2 + (self.b)*x +(self.c)

    def get_roots(self) :
        d = (self.b**2) - (4*self.a*self.c)
        
        sol1 = (-self.b -cmath.sqrt(d))/(2*self.a)
        sol2 = (-self.b +cmath.sqrt(d))/(2*self.a)
        
        print(f"solution: {sol1}, {sol2}")

e= Quadratic(1, 5, 6)
e.get_roots()