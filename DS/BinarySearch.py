#Binary function in Python - Version 2.7
#This function will search for an item in a list
def BinarySearch(num,numList):
    found = False #Initialize found as false
    bottom = 0 #Initialize bottom as zero
    top = len(numList) - 1 #Initialize top as the position of last element in the list
    while bottom <= top and not found: #Run a loop till start posistion is less than or equal to the end position and found is not true. 
        middle = (bottom+top)//2 #Find middle element position by adding starting and ending position and divide it by 2
        if numList[middle]==num: #If the middle element is equivalent to the number we are finding return found as true
            found = True
        elif numList[middle] < num: #Else check if the middle element is less than the number we are finding that implies the number is between middle and top. So assign middle as bottom.
            bottom = middle + 1
        else:
            top = middle - 1 #Else check if the middle element is greater than the number we are finding that implies the number is between bottom and middle. So assign middle as top.
    return found

def main():
    numberList = [1,2,4,5,6,7,23,43,56,67,89,98,876] #Ordered List
    number = int(raw_input("What number are you looking for in the list? "))
    isitFound = BinarySearch(number,numberList)
    if isitFound:
        print "Number is in the list"
    else:
        print "Number is not in the list"

if __name__=='__main__':
   main()
