#Program to reverse a string
#String input by User
#Python 3
def revString(myString):
    # Method1 - Slicing.
    # With indexing we manipulate or return a single item but with Slicin we can manipulate multiple items.
    # To access parts of sequences like strings, tuples, and lists is known as slicing in Python.
    # There are two variants of the slicing syntax: sequence[start:stop] and sequence[start:stop:step]
    print("\nReversed string using Slicing method is: ",myString[::-1])
    # Method2 - With Loop
    reverseString=[] # Declared Null Array for reverse string
    index = len(myString) # Calculating the length of string
    while index > 0:
        reverseString += myString[index -1]
        index -= 1
    finalString = ""
    print("\nReversed string using index method is: ",finalString.join(reverseString))
    # Method2 - With Join and Reverse function of string
    reversedString = ''.join(reversed(myString))
    print("\nReversed string using Join method is:",reversedString,"\n")
def main():
    userInput = input("Enter the string to be reversed:\n")
    inputType = type(userInput)  #Finding out datatype of input string
    print("\nUser input is: ",userInput)
    print("\nData type of user input is: ",inputType)
    revString(userInput)

if __name__=='__main__':
    main()
