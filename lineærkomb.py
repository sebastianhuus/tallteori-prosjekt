from sff import finn_sff
from euklid import *

tall1 = 513
tall2 = 153

# sa+tb
sff = finn_sff(tall1,tall2)
if sff > 1:
    tall1 //= sff
    tall2 //= sff


# hm nei dette var slitsomt