def check(a, b):
    if(len(a) != len(b)):
        return False
    elif(sorted(list(a)) == sorted(list(b))):
        return True
    else:
        return False


def main():
    list1 = ['a', 'b', 'c', 'd']
    list2 = ['d', 'b', 'a', 'c']
    str1 = 'abcd'
    str2 = 'cdba'
    print(check(str1, str2))
    result = check(list1, list2)
    if result:
        print("Given strings are Anagram")
    else:
        print("Given strings are not Anagram")


if __name__ == '__main__':
    main()
