# Finner sff mellom to tall
def euklid(a,b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


# Euklids utvidede algoritme, stjålet fra en smart sjel på internettet
def utvidet(a,b):
    if a == 0:
        return b, 0, 1
    else:
        sff, s, t = utvidet(b % a, a)
        return sff, t - (b // a) * s, s
