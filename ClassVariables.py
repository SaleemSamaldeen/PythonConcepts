class Employee:

    experience = 11   #class variables. also known as static variables

    def __init__(self):
        self.number = 5001    #instance variables
        self.designation = "Software analyst"   #instance variables

employee = Employee()
juniorEmp = Employee()

employee.number = 5412
juniorEmp.number = 1234
Employee.experience = 5  #class variables can be accessed via class itself and affect also values in objects

print(employee.number, employee.designation, employee.experience)
print(juniorEmp.number, juniorEmp.designation, juniorEmp.experience)