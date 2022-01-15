# Program to display basic List functionalities in Python3
def main():
    try:
        fileObject = open('SampleText.txt', 'rt')
        data = fileObject.read()
        data = data.replace('Mukul', 'MUKUL')
        fileObject.close()
        fileObject = open('SampleText.txt', 'wt')
        fileObject.write(data)
        fileObject.close()
        f1 = open("file3.lst", "r")
        f3 = open("file2.txt", "w")
        data = f1.readlines()
        for x in data:
            print(x)
        print(len(data))
        i = len(data) - 1
        while i >= 0:
            f3.write(data[i])
            i = i - 1
        f1.close()
        f3.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
