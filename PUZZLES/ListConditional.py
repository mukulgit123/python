# Custom input for Test Case 0
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
if __name__ == '__main__':
    N = int(input())
    myList = [ x for x in range(N)]
    executeCmd = []
    runCLI = True
    while(runCLI):
        try:
            executeCmd = input().split()
        except EOFError as e:
            print(e)
        if executeCmd[0] == 'insert':
            myList.insert(int(executeCmd[2]),int(executeCmd[1]))
        elif executeCmd[0] == 'print':
            print(myList)
        elif executeCmd[0] == 'remove':
            myList.remove(int(executeCmd[1]))
        elif executeCmd[0] == 'append':
            myList.append(int(executeCmd[1]))
        elif executeCmd[0] == 'sort':
            myList.sort()
        elif executeCmd[0] == 'pop':
            myList.pop(len(myList) - 1)
        elif executeCmd[0] == 'reverse':
            myList.reverse()
        else:
            runCLI = False
