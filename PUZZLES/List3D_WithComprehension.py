#Python3 - Print a 3d array with x,y,z and use List comprehensions to print another one where sum of x,y and z is not
#equal to n
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    listPermutations=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                listPermutations.append([i,j,k])
    #print(listPermutations)
    xyzNotEqualN = [ p for p in listPermutations if sum(p)!=n ]
    print(xyzNotEqualN)
