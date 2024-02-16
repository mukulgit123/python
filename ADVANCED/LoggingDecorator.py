def logged(function):
    def wrapper(*args, **kwargs):
        return_value = function(*args, **kwargs)
        with open('logfile.txt','a+') as f:
            fname = function.__name__
            print(f"{fname} has return value {return_value}")
            f.write(f"{fname} has return value {return_value}\n")
        return return_value
    return wrapper

@logged
def add(x,y):
    return x+y

print(add(10,50))
