#Linear Search function in Python - Version 2.7
#This function will search for an item in a list
#Time Complexity O(n)
#Space Complexity O(1)
def LinearSearchSentinal(myItem,myList):
    position = 0 #Index to store the location where item will be found
    myList.append(str(myItem))
    for i in range(len(myList)-1):
        if myList[i] == myList[len(myList)-1]:
            position = i+1
    return position # return found at the end

def main():
    shopping = ["apple","banana","chocolate","pasta"]
    item = raw_input("What do you want to find? ")
    position = LinearSearchSentinal(item,shopping)
    if position!=0:
        print str(item) + " is found in the list at " + str(position)
    else:
        print "Our item is not in the list"

if __name__=='__main__':
   main()
