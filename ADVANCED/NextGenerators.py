def mygenerator(n):
    for x in range(n):
        yield x ** 3


values = mygenerator(90000)

print(next(values))

print(next(values))

print(next(values))

print(next(values))

print(next(values))

print(next(values))


print(next(values))

print(next(values))
