class Parent:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def config(self):
        print(f"The value of username is: ", self.username + " " + self.password)

parent = Parent("Python",password="Developer") # either assign value or just given arguments alone
parent.config()