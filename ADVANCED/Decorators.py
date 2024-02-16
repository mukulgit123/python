def mydecorator(function):
    def wrapper(*args, **kwargs):
        function(*args, **kwargs)
        print("I have been decorated.")
    return wrapper

@mydecorator
def hello_world():
    print("Hello World!!")

@mydecorator
def hello(person):
    print(f"hello {person}")


@mydecorator
def hello_return(person):
    print(f"hello {person}")
hello_world()

hello("mukul")

hello_return("mike")
