class FunctionConcepts:

    @staticmethod
    def get_username(f_name, l_name): #To have static method, declare with staticmethod annotation
        f_name = f_name.capitalize()
        l_name = l_name.capitalize()
        return f_name + " " + l_name

function = FunctionConcepts() # to create an object for a class

print(f'The user name is {function.get_username("John", "Smith")}') #calling method via object
print(f"The Username is via static method: ", FunctionConcepts.get_username("python", "function")) #If static no need to use an object to call a method
