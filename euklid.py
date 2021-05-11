# Finner sff mellom to tall
def euklid(a,b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a
