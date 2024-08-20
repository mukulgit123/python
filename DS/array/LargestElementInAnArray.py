def main():
    arr = [2, 3, 4, 5, 1]
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    print(max)


if __name__ == '__main__':
    main()
