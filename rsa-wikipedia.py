from euklid import *
from primtall import liste as alleprimtall
from bokstaver import småbokstaver, storebokstaver

p = 61
q = 53


n = p*q

phi = (p-1)*(q-1)

# e og phi skal være innbyrdes primske.
e = alleprimtall[32]

# d*e = 1 (mod phi)
x = 4
d = (1 + x*phi) % e

print((n,phi,e,d))
