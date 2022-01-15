import random
import time


def speed_test(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        for x in xrange(5000):
            results = func(*args, **kwargs)
        t2 = time.time()
        print '%s took %0.3f ms' % (func.func_name, (t2 - t1) * 1000.0)
        return results
    return wrapper


@speed_test
def compare_bitwise(x, y):
    set_x = frozenset(x)
    set_y = frozenset(y)
    return set_x & set_y


@speed_test
def compare_listcomp(x, y):
    return [i for i, j in zip(x, y) if i == j]


@speed_test
def compare_intersect(x, y):
    return frozenset(x).intersection(y)


# Comparing short lists
a = [1, 2, 3, 4, 5]
b = [9, 8, 7, 6, 5]
compare_bitwise(a, b)
compare_listcomp(a, b)
compare_intersect(a, b)

# Comparing longer lists
a = random.sample(xrange(100000), 10000)
b = random.sample(xrange(100000), 10000)
compare_bitwise(a, b)
compare_listcomp(a, b)
compare_intersect(a, b)
