class Company:
    def __init__(self, name, address):
        self.name=name
        self.address=address
    
    def info(self):
        print(f"Company name is {self.name}, address is {self.address}")
        
class Finance(Company):
    def __init__(self, name, address, worth):
        super().__init__(name, address)
        self.worth=worth
    
    def compnyworth(self):
        print(f"{self.name} is in {self.address} and its worth is {self.worth}")

class Employee(Finance,Company):
    def __init__(self,name, address, worth, empname):
        super().__init__(name,address, worth)
        self.empname=empname
    def emp_info(self):
        print(f"i am {self.empname} an employee of {self.name} company, which is in {self.address}, whose worth is {self.worth}.")

c1=Company("Alphabridge","Lahore")
f1=Finance("Alphabridge","Dha-6",56000000)
e1=Employee("Aplhabridge","DHA-6 Lahore","120000000","Ahmed")


c1.info()
f1.compnyworth()
f1.info()
e1.info()
e1.compnyworth()
e1.emp_info()
