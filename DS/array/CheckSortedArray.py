def checkSortedArray(arr):
    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True

def main():
    arr = [1,2,2,3,4,5]
    print(checkSortedArray(arr))

if __name__ == '__main__':
    main()