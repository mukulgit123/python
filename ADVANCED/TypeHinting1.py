def myfunction(parameter: int) -> str:
    return f"{parameter+10}"

def myotherfunction(parameter2: str):
    print(parameter2)

print(myfunction(10))

myotherfunction(myfunction(20))

def dosth(param: list[int]): #Works only with Python 3.9
    for i in range(len(param)):
        print(param[i])

a = [1,2,3,4,5,6]
dosth(a)