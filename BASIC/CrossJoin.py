#Program to create a cross joined Array of 2X2 and find the sets whose sum is Zero

def main():
    firstList = [52,14,23,18,22,8,189,98]
    secondList = [72,-14,84,-98,77,-22]
    crossjoin = []
    result = []
    try:
        for i in range(len(firstList)):
            for j in range(len(secondList)):
                crossjoin.append((firstList[i],secondList[j]))
                if firstList[i] + secondList[j] == 0:
                    result.append((firstList[i],secondList[j]))
        print(crossjoin) 
        print(result)
    except Exception as e:
        print(e)
if __name__ == '__main__':
    main()

#Output

#[(52, 72), (52, -14), (52, 84), (52, -98), (52, 77), (52, -22), (14, 72), (14, -14), (14, 84), (14, -98), (14, 77), (14, -22), (23, 72), (23, -14), (23, 84), (23, -98), (23, 77), (23, -22), (18, 72), (18, -14), (18, 84), (18, -98), (18, 77), (18, -22), (22, 72), (22, -14), (22, 84), (22, -98), (22, 77), (22, -22), (8, 72), (8, -14), (8, 84), (8, -98), (8, 77), (8, -22), (189, 72), (189, -14), (189, 84), (189, -98), (189, 77), (189, -22), (98, 72), (98, -14), (98, 84), (98, -98), (98, 77), (98, -22)]

#[(14, -14), (22, -22), (98, -98)]
