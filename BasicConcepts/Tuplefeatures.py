class TupleFeatures:

    # Immutable, so values can't be changed and iteration is faster than list

     noOfStudents = (8,9,7,6,4,7,2,3)
     print( 'Total no of repeated values in tuple: ',noOfStudents.count(7))

     print('Get the index of any number in Tuple: ', noOfStudents.index(4))