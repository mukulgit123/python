# Program to display basic Dictionary functionalities in Python3
def main():
    dict = {}
    dict['key1'] = "Value One"
    dict['key two'] = "Value 2"
    tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
    try:
        print("Dictionary - Keys: ", dict.keys())
        print("Dictionary - Values: ", dict.values())
        print("Dictionary - Printing Value 1: ", dict.get('key1'))
        print("Tiny Dict is here: ", tinydict.keys(), tinydict.values())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
