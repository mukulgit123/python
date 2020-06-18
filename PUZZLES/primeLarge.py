def prime(x):
    count = 0
    for i in range(1,x):
            if x % i == 0:
                count = count+1
    if count > 1:
        return False
    else:
        return True
    
def primeLarge(n):
    for i in range(int(n)+1):
        primeList = []
        if prime(i):
            primeList.append(i)
        else:
            pass
    print(prime)

def main():
    a = input("Enter the number")
    if int(a) < 2 and len(a) < 1 and len(a) >= 10**5:
        print("Constraints failed.")
    else:
        primeLarge(a)
        #rint(k)

if __name__=='__main__':
    main()
