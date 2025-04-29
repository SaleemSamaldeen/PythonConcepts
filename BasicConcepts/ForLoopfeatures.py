class ForLoopfeatures:
    def __init__(self):
        print("For Loop features are: ")

    def get_OddNumbers(self):
        print("Odd numbers are: ",end = ' ')
        for i in range(1,10):
            if i%2 != 0:
                print(i,end = ' ')

    def printPatterns(self):
        print('\nPatterns are: ')
        for i in range(1,11):
            for j in range(1,i+1):
                print('*', end = ' ')
            print()

    def printReversePatterns(self):
        print('\nReverse Patterns are: ')
        for i in range(1,11):
            for j in range(0,11-i):
                print('*', end = ' ')
            print()

forloopfeatures = ForLoopfeatures()
forloopfeatures.get_OddNumbers()
forloopfeatures.printPatterns()
forloopfeatures.printReversePatterns()