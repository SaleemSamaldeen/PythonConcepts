class ListFeature:
    # CTRL + SHIFT + F10 to run all files

    #List is mutable, as we can change values
    numbers = list() # Initialize an empty list

    numbers.append(45) #use append to add all elements
    numbers.append(85)
    numbers.append(12)
    numbers.append(93)
    numbers.append(15)
    numbers.append(23)

    print('The minimum number is ', min(numbers))  # Default methods in list python

    print('The maximum number is ', max(numbers))  # Default methods in list python

    print('The average number is ', round(sum(numbers) / len(numbers), 2))  # Default methods in list python

    print('The sum of numbers is ', sum(numbers))  # Default methods in list python

    print('The length of numbers', len(numbers))  # Default methods in list python

    # To sort the list
    print('The sorted numbers are', numbers.sort())  # Default methods in list python

    # To reverse the list
    print('The reversed numbers are', numbers.reverse())  # Default methods in list python

    print('The index of any particular value in the list: ',
          numbers.index(93))  # Get index of any particular value in the list

    marks = [55, 90, 100, 65, 38]
    mixed = [numbers, marks]
    print('Two combined list is: ', mixed)  # Two list can be combined

    marks.append('python') #Append can be used to add one value at the end of list
    print('After append the values in marks: ', marks)  # Append will add value at the end of list in python

    marksOfStudents = list()
    marksOfStudents.append(22.7)
    marksOfStudents.append(65)
    marksOfStudents.append('allStudents')

    marks.extend(marksOfStudents) #Extend can add multiple values in the list
    print('After extending the values in marks: ', marks)  # Extend will add value at the end of list in python

    marks.insert(2, 95)
    print('After insert the values in marks: ', marks)  # Insert any value with index and object you want to perform

    print('To get total no of values present in the list, use count:', marks.count(65))

    marks.remove(55)
    print('After remove the values in marks: ', marks)  #Remove any particular value form the list

    marks.pop(1) #With index, Pop remove element from the list
    print('Pop is used to remove any value using index in list: ',marks)

    marks.pop()
    print('After using pop method for the list: ', marks) #Without index, Pop always remove last element added in the list

    copied = marks.copy()
    copied.append('copied')
    print('To get the copy of the exact list: ',copied)

    del copied[0] #Delete value form index 0
    print('After deleting first index from a copy of the exact list: ',copied)

    del copied[4:] #Delete all values from index 4
    print('After deleting all values from index 4 from a copy of the exact list: ',copied)

    marks.clear()
    print('After clearing the list: ', marks) #Clear used to clear all values from list







