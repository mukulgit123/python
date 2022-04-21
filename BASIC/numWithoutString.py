import math
if __name__ == '__main__':
    n = int(input())
    my_num = 0
    for i in range(1,n+1):
        digits = int(math.log10(i))+1  
        my_num = my_num * (10 ** digits) + i
    print(my_num)  
