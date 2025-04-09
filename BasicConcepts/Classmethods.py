class Students:

    schoolName = "Python Concepts"

    def __init__(self, mark, totalSubject, students):
        self.mark = mark
        self.totalSubject = totalSubject
        self.students = students

    def getAverage(self):    #instance method
        return (self.mark + self.totalSubject + self.students) / 3

    @classmethod
    def getSchoolName(cls):   #class method
        print(f"The school name is {cls.schoolName}")

    @staticmethod
    def genericMethod(email, otp):  #static method
        print(f"This generic method can perform any action {email} and {otp}")

student1 = Students(54,6,30)
student2 = Students(100,6,50)

print(student1.getAverage())
print(student2.getAverage())
Students.getSchoolName()
Students.genericMethod("test@gmail.com",1234)