from datetime import datetime

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29,
        31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

right_this_minute = datetime.today().minute

right_this_hour = datetime.today().hour

for numTimes in range(5):
    if right_this_minute in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")

    if right_this_hour in odds:
        print("This hour is an odd hour.")
    else:
        print("Not an odd hour.")
