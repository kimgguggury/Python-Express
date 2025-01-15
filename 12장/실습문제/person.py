class Person :
    def __init__(self, name, number) :
        self.name = name
        self.number = number

class Student(Person) :
    def __init__(self, name, number, classes, gpa) :
        super().__init__(name, number)
        self.classes = []
        self.classes.append(classes)
        self.gpa = gpa
        
    def __str__(self) :
        return "이름="+self.name+"\n주민번호="+str(self.number)+\
            "\n수강과목="+str(self.classes)+"\n평점"+str(self.gpa)

class Teacher(Person) :
    def __init__(self, name, number, coures, salary) :
        super().__init__(name, number)
        self.coures = []
        self.coures.append(coures)
        self.salary = salary
        
    def __str__(self) :
        return "이름="+self.name+"\n주민번호="+str(self.number)+\
            "\n강의과목="+str(self.coures)+"\n월급"+str(self.salary)

s1 = Student("홍길동",1234567,"자료구조",0)
print(s1)
print()
t1 = Teacher("김철수",12345678,"Python",300)
print(t1)