#Linear Search function in Python - Version 2.7
#This function will search for an item in a list
def LinearSearch(myItem,myList):
    found = False #Initially item is not found
    position = 0 #Index to store the location where item will be found
    while position < len(myList) and not found: #Till position is less than length of list and found is not true
        if myList[position] == myItem: #if the item at iterated position is equal to the item being searched mark found as true.
            found = True
        position = position + 1
    return found # return found at the end

def main():
    shopping = ["apple","banana","chocolate","pasta"]
    item = raw_input("What do you want to find? ")
    isitFound = LinearSearch(item,shopping)
    if isitFound:
        print "Item is in the list"
    else:
        print "Item is not in the list"

if __name__=='__main__':
   main()
