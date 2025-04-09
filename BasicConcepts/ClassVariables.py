class Employee:

    experience = 11   #class variables. also known as static variables
    age = 0

    def __init__(self):  #Constructor in python always start with __init__
        self.number = 5001    #instance variables
        self.designation = "Software analyst"   #instance variables

    def setAge(self,age):
        self.age = age

    def getAge(self):
        return self.age

    def config(self):
        print(self.number, self.designation)

employee = Employee() # To create an object for a class
juniorEmp = Employee() # To create an object for a class

employee.number = 5412
juniorEmp.number = 1234
Employee.experience = 5  #class variables can be accessed via class itself and also affect values in objects
employee.setAge(45) #encapsulation

print(employee.number, employee.designation, employee.experience)
print(juniorEmp.number, juniorEmp.designation, juniorEmp.experience)
juniorEmp.config()
print(employee.getAge(), juniorEmp.getAge())