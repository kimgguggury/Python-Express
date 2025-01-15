class Sprite :
    def __init__(self, x, y, image) :
        pass
    
    def draw(self) :
        raise NotImplementedError("이것은 추상클래스")
    
    def move(self) :
        raise NotImplementedError("이것은 추상클래스")
    
class Alien(Sprite) :
    def __init__(self, x, y, image, speed) :
        super().__init__(x, y, image)
        self.speed = speed
        
    def move(self) :
        self.x += self.speed
        self.y += self.speed

class Player(Sprite) :
    def __init__(self, x, y, image, name) :
        super().__init__(x, y, image)
        self.name = name
        
    def move(self) :
        pass

a = Alien(0, 100, "image1.jpg", 10)
p = Player(0, 100, "image1.jpg", "player1")