def averageResponse(avgResp, count):
    ar = avgResp / count
    return(ar)


def main():
    try:
        totalResponse = 0
        count = 0
        logFile = open("access.log", "r")
        log = logFile.readlines()
        for x in log:
            if "/test" in x:
                k = x.split(" ")
                totalResponse += float(k[5])
                count += 1
        logFile.close()
        ar = averageResponse(totalResponse, count)
        print("Average response time for test api is: ", ar)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
