# This program is written in Python version 3 to calculate the angle between hour and minute hand
# 

def calculateAngle(hour,minute):
    m = int(minute)
    h = int(hour)
    mangle=6 #Angle between each minute is 6 degrees
    hangle=30 # Angle between each hour is 30 degrees
    a = int(hangle * h )
    b = int(mangle * m)
    print(a,b)
    angle = int(m * mangle) - int(h * hangle)
    return angle

def main():
    time = input("Enter the time for calculing the angle:\nFormat to be used: hour.minute\n")
    hour_minute=time.split('.')
    a = calculateAngle(hour_minute[0],hour_minute[1])
    print("Minute and hour hand are making an angle of ",a," degrees")

if __name__=='__main__':
    main()
