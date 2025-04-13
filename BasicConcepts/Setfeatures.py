class Setfeatures:

# No duplicates allowed and unordered collections | indexing not supported in set as we don't follow proper sequence

# A set is mutable, i.e., we can remove or add elements to it.

# Items of a set in python are immutable (unchangeable), do not duplicate values, and unordered.
# Thus, items in a set do not appear in a stipulated manner, i.e., they can appear in a different order every time it is used.
# Due to this, set items cannot be referred to by key or index.
# After a set is created, its items cannot be changed. However, new items can be added.
# As we mentioned, all set items need to be unique because duplicates are not allowed. Items in a set can be of any data type.
# Set items can be of any data type: String, Boolean, tuple, float, int

    noOfMarks = set()  #initialze an empty Set

    noOfMarks.add(85)
    noOfMarks.add(95)
    noOfMarks.add(41)
    noOfMarks.add(65)
    noOfMarks.add(12)
    noOfMarks.add(23)
    print('Total no of marks in set:', noOfMarks)

    noOfMarks.pop() #Pop always remove last element added in the list
    print('Total no of marks in set after pop method:', noOfMarks)

    #noOfMarks.pop(2) ----> indexing is not supported in Set

    noOfMarks.remove(23) #Remove any element from Set
    print('Total no of marks in set after remove method:', noOfMarks)

    noOfMarks.add('pythonSet')
    print('Total no of marks in set after add method:', noOfMarks)

    secondSetOfMarks = set()
    secondSetOfMarks.add(45)
    secondSetOfMarks.add(61)
    noOfMarks.update(secondSetOfMarks) # Update is used to add another set (update the set with union of others and itself)
    print('Total no of marks in set after update method:', noOfMarks)
