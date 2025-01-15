class Employee :
    def __init__(self, name="", salary = 0) :
        self.name = name
        self.salary = salary
    
    def getSalary(self) :
        return self.salary 
    

class Manager(Employee) :
    def __init__(self, name, salary, bonus=0) :
        super().__init__(name, salary)
        self.bonus = bonus
    
    def getSalary(self):
        salary = super().getSalary()
        return salary + self.bonus
    
def main () :
    employee = Employee("하나",100)
    manager  = Manager("김동현",100,10)
    print("직원의 월급 : "+str(employee.getSalary()))
    print("매니저의 실수령액 : "+str(manager.getSalary()))

main()
    