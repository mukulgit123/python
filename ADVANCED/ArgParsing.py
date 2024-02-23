def myfunction(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(kwargs['KEYONE'])
    print(kwargs['KEYTWO'])

myfunction('HEJAAA', True, 19, "WOW", KEYONE="TRAM2", KEYTWO="TRAM3")