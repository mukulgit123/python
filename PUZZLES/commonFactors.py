# Write your code here
def bigger(x,y):
    if(x>y):
        return(x)
    else:
        return(y)

def factors(a,b):
    big = int(bigger(a,b))
    common_factors = []
    i=0
    while( i < big):
        i+=1
        if(int(a) % i == 0 and int(b) % i == 0):
             common_factors.append(i)
    return(common_factors)
                
def main():
    a = input("Enter the first number:\n")
    b = input("Enter the second number:\n")
    begin = 1
    end = 10**12
    if( int(a) >= begin and int(a) <= end and int(b) >= begin and int(b) <= end):
        list = factors(a,b)
        cf = len(list)
        print("Common factors of ",a," and ",b," are ",cf," : ", list)
    else:
        print("Constraints do not match")

if __name__=='__main__':
    main()

