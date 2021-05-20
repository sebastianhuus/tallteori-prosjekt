from sff import finn_sff
from euklid import *
from timeit import default_timer as timer

a = 1319
b = 1848

def test(algo):
    start = timer()

    algo(a,b)

    end = timer()
    diff = end - start

    print(diff)

    return diff


t1 = test(euklid)
t2 = test(finn_sff)

print(t2/t1)