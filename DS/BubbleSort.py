# BubbleSort function in Python - Version 2.7
# This function will sort a List based on bubblesort algorithm
def BubbleSort(myList):
    moreSwaps = True  # Initially swaps needed flag will be true
    while moreSwaps:  # Run loop while more swaps are required i.e. moreSwaps is true
        # Before looping mark moreSwaps as false so that if no swap happens in
        # the loop then it can break out of the while loop.
        moreSwaps = False
        for element in range(len(myList) - 1):
            if myList[element] > myList[element + 1]:
                moreSwaps = True  # Swap condition found
                myList[element], myList[element +
                                        1] = myList[element + 1], myList[element]
    return myList  # return sorted list at the end


def main():
    unsortedList = [8, 2, 72, 4, 65, 6]
    print "Unsorted List is: " + str(unsortedList)
    sortedList = BubbleSort(unsortedList)
    print "Sorted List is: " + str(sortedList)


if __name__ == '__main__':
    main()
