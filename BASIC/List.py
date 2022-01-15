# Program to display basic List functionalities in Python2.7
def main():
    firstList = [52, 14, 23, 18, 22, 8, 8, 189, 8]
    print "Original List: " + str(firstList)
    try:
        firstList.append(786)  # Appends an item at the end of the list
        print "Appended list: " + str(firstList)
        # firstList[len(firstList)+2] = 56 - Commented section for creating
        # exception.
        firstList.sort()
        print "Sorted List: " + str(firstList)
        # removes last element on the list or the one at mentioned index
        popped = firstList.pop()
        print "An item " + str(popped) + " has been removed from the list"
        print "New list after item removal is: " + str(firstList)
        firstList.remove(14)
        print "New list after 14 is removed: " + str(firstList)
        copiedList = firstList
        print "Copied list is " + str(copiedList)
        countOf = firstList.count(8)
        print "8 has been repeated " + str(countOf) + " times in the list"
        copiedList.extend(firstList)
        print "This is my new Copied List " + str(copiedList)
        copiedList.remove(8)  # Removes first occurence of an item
        print "Removed first occurence of 8 from copied list: " + str(copiedList)
        copiedList.sort()
        # Clear function doesn't run on Python2.7 but we can clear a list like
        # this
        del copiedList[:]
        print "Empty list can still be printed as: " + str(copiedList)
    except Exception as e:
        print e


if __name__ == '__main__':
    main()
