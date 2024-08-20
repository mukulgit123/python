def secondLargest(arr):
    largest = arr[0]
    secondLargest = int(-1e9)
    for i in range(1, len(arr)):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > secondLargest:
            secondLargest = arr[i]
    return secondLargest


def secondSmallest(arr):
    smallest = arr[0]
    secondSmallest = int(1e9)
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            secondSmallest = smallest
            smallest = arr[i]
        elif arr[i] > smallest and arr[i] < secondSmallest:
            secondSmallest = arr[i]
    return secondSmallest


def main():
    arr = [1, 2, 4, 7, 7, 5, 19, 13, 16, 15]
    sLargest = secondLargest(arr)
    sSmallest = secondSmallest(arr)
    print(sLargest)
    print(sSmallest)


if __name__ == '__main__':
    main()
