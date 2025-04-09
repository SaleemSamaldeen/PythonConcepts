#Data types in python:
#Null
#Numeric - int, float, complex, bool
#Sequqence - String, List, Tuple, Set, String, Range
#Dictionary (Mapping)
#Unfortunately creating a constant variable not possible in Python

#Number
number = 5
print('To get the type of int dataType', type(number))
print('To convert int value to float data type', float(number))

#float
floatValue = 5.5
print('To get the type of float dataType', type(floatValue))
print('To convert float value to int data type', int(floatValue))

#complex
complexExample = 6+4j
complexValue = complex(number,floatValue) #Combine any two number to get complex
print('To get complex output',complexValue)
print('To get the type of complex dataType',type(complexValue))
print('To get the type of complex dataType',type(complexExample))

#bool
boolValue1 = True
boolValue2 = False

print('To get the type of bool dataType',type(boolValue1))
print('To get the int value of bool value TRUE',int(boolValue1))
print('To get the int value of bool value FALSE',int(boolValue2))

#String
name = 'Python developer'
singleChar = 's'
print('To get the type of String dataType:' , type(name))
print('To get the type of char dataType, which is also String:' , type(singleChar))

#list
noOfStudents = [8,9,7,6,4,7,2,3]
print('To get type of list dataType',type(noOfStudents))

#tuple
tupleExample = (8,9,7,6,4,7,2,3)
print('To get the type of tuple dataType',type(tupleExample))
print('To get the value from Tuple: ',tupleExample[0])

#set
setExample = {8,9,7,6,4,7,2,3} #remove duplicates and unordered collections
print('All values from set:', setExample)
print('To get the type of set dataType',type(setExample))

#range
rangeExample = range(51) #have range till number upto 51
specificRange = range(0,25,5) #have range with specific interval as third argument
print('To get the type of range dataType',type(rangeExample))
print('Convert range into list:', list(rangeExample))
print('Convert range into list:', list(specificRange))
print('Get value from rangeExample:', rangeExample[8])
print('Get value from specificRange:', specificRange[3])

#dictionary
mapping = {'TCS':'Kalai', 'Infy': 'Deepak', 'Backend': 'Vishnu'} #key value mapping like Java map
print('To get the type of dictionary dataType',type(mapping))
print('Get all from mapping:', mapping)
print('Get all keys from mapping:', mapping.keys())
print('Get all values from mapping:', mapping.values())
print('Get value from specific key mapping:', mapping.get('Backend'))
print('Get value from secific key mapping:', mapping['Infy'])



