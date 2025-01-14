class Book :
    def __init__(self,title = '',pages = 0) :
        self.title = title
        self.pages = pages
    
    def  __gt__(self,other) :
        return self.pages > other.pages
        
    def __str__(self) :
        return self.title

boo1 = Book('Magic of Python', 600)
boo2 = Book('Master of Python', 700)

print(boo1 > boo2)
print(boo1)