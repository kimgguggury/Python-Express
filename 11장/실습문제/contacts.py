# class Person :
#     def __init__(self,name,age) :
#         self.name = name
#         self.age = age
#     def __repr__(self) :
#         return "<이름 :%s. 나이 :%s>" %(self.name, self.age)

# def keyAge(person) :
#     return person.age    
# people = [Person("홍길동",54), Person("김동현", 26), Person("송철웅", 32)]
# print(sorted(people, key= keyAge))


data = [ (3, 100), (1, 200), (7, 300), (6, 400) ]
tmp = sorted(data, key=lambda item : item[0])
print(tmp)