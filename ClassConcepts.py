class Parent:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def config(self):
        print(f"The value of username is: ", self.username + " " + self.password)

    def compare(self, other):
        if self.username == other.username:
            return True
        else: return False

parent = Parent("Python", password="Developer")  #either assign value or just given arguments alone
child = Parent("Python","Junior")
parent.config()

if parent.compare(child):
    print("Both are same")
else: print("They are different")

if parent == child:
    print("Both object are same")
else: print("They are different")