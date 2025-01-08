# class Television: 
#     def __init__(self, channel, volume, on) :
#         self.channel = channel
#         self.volume = volume
#         self.on = True
    
#     def show(self) :
#         print(self.channel, self.volume, self.on)
    
# def setSilentMode(t) :
#     t.volume = 2

# myTv = Television(11, 10, True)
# setSilentMode(myTv)
# myTv.show()

class Television :
    serialNumber = 0 
    
    def __init__(self, channel, volume, on) :
        self.channel = channel
        self.volume = volume
        self.on = on
        Television.serialNumber += 1
        self.number = Television.serialNumber
    
    def show(self) :
        print(self.channel, self.volume, self.on, self.number)

myTv = Television(11, 10, True) 
myTv.show()