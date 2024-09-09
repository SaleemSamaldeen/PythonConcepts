name = 'Python Developer Stage'
result = "Python" in name    # To check if value present or not which returns boolean
splitted = name.split(" ") #to split based on limiters
replaceText = name.replace("Developer", "Beginner")  #to replace the text
count = len(name)   #to find the length of the string
upperCase = name.upper() #to convert uppercase
lowCase = name.lower()  #to convert lowercase
firstLetterCapital = name.capitalize() # to capitalize only first letter
leftStrip = name.lstrip("Python ") #

print(leftStrip)
print(result)
print(splitted)
print(replaceText)
print(count)
print(firstLetterCapital)
print(upperCase)
print(lowCase)
print(name)
print("To get number of word occurrences: ", name.count("Stage"))
print("To get starting index of Stage: ", name.index("Stage"))
print("To get starting index of Stage", name.find("Stage"))
print("To get first occurrence of letter o: ", name.find("o"))
print("To get last occurrence of letter o: ", name.rfind("o"))
print("To get no occurrence of letter z: ", name.rfind("Z"))  # if there are no occurrences, ans is -1
print("Substring of given string: ", name[0:name.index("Stage")])