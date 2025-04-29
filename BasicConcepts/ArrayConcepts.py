from array import array


class ArrayConcepts:
    noOfCities = array('i', [7, 9, 3, 4, 6]) # 'i' is the type code for signed integer
    print('After array creation',list(a for a in noOfCities))

    noOfCities.append(1)  #To add value at the end of array
    print('After adding value at the end of array',noOfCities)

    noOfCities.insert(2, 5)  #To insert value at specific index
    print('After inserting value at the end of array',noOfCities)

    noOfCities.remove(1)  #To remove value from array
    print('After removing value from array',noOfCities)

    noOfCities.pop()  #To remove last value from array using pop method
    print('After using pop method in array',noOfCities)

    noOfCities.pop(2)  #To remove value from specific index using pop method
    print('After using pop method with specific index in array',noOfCities)

    noOfCities.reverse()  #To reverse the array
    print('After reverse method using reversed array',noOfCities)

    print('Type code of array:',noOfCities.typecode)  #To get the type code of array

    print('Array buffer info',  noOfCities.buffer_info())