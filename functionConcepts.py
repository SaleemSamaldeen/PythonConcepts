def getUserName(fName, lName):
    fName = fName.capitalize()
    lName = lName.capitalize()
    return fName + " " + lName

print(f"The Username is: ", getUserName("python","function"))
