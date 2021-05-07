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

test(euklid)
test(finn_sff)