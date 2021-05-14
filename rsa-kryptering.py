# sff(e, (p-1)(q-1)) = 1
# e er krypteringseksponenten. Større enn 2.
# p og q er to odde primtall med produkt større enn 30

from euklid import *
from primtall import liste as alleprimtall
from bokstaver import småbokstaver, storebokstaver


# SFF skal være lik 1, ellers funker dette ikke
def test_gyldighet():
    e = alleprimtall[5]
    p = alleprimtall[12]
    q = alleprimtall[23]
    print(euklid(e, (p-1)*(q-1)))


# Kryptering
# b = a^e mod n
# b er den krypterte versjonen av det vi sender. Edit: dette her var myyyye lettere enn for hånd jo.
def krypter(a,e,n):
    b = a**e % n
    return b


def bokstav_til_tall(bokstav):
    allebokstaver = småbokstaver + storebokstaver
    if bokstav not in allebokstaver:
        return None

    for i in range(len(småbokstaver)):
        if småbokstaver[i] == bokstav:
            return i

    for i in range(len(storebokstaver)):
        if storebokstaver[i] == bokstav:
            return i

def krypter_bokstav(bokstav, e, n):
    b = bokstav_til_tall(bokstav)
    return krypter(b, e, n)


# d*e = 1 mod (p-1)(q-1). Her må vi ha en egen algo for euklids utvidede.
def dekrypter(e, p, q):
    utvidet(p, q)

    r = e % (p-1)*(q-1)
    return r

e = 3
n = 55

b = krypter_bokstav("s", e, n)
print(b)


