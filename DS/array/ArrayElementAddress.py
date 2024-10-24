from ctypes import c_int, addressof  # importing c_int and addressof from ctypes


def main():
    arr = [1, 2, 3, 4, 5]
    print(id(arr[0]))  # printing the address of the first element of the array
    # printing the address of the second element of the array which has a
    # difference of 32 bits from the the previous one
    print(id(arr[1]))
    print(id(arr[2]))
    print(id(arr[3]))
    print(id(arr[4]))
    print(id(arr))


if __name__ == '__main__':
    main()
