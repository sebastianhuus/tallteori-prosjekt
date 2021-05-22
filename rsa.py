from euklid import *

p = 2
q = 7
n = p*q
phi = (p-1)*(q-1)

# 1 < e < phi
# sff(e,n) = 1, sff(e,phi) = 1
# Dette er alle verdier i intervallet som e er i.
muligeE = []
for i in range(2,phi):
    muligeE.append(i)


# Nå må vi fjerne tall med felles faktorer med n og phi
def fjern_multiplum(liste, n):
    alletall = []
    for i in range(1, int(n)):
        alletall.append(i)

    for tall in alletall:
        if (n % tall == 0 or euklid(tall, n) > 1) and tall in liste:
            liste.remove(tall)

    return liste


muligeE = fjern_multiplum(muligeE, phi)
muligeE = fjern_multiplum(muligeE, n)

from random import randint

indeks = randint(0, len(muligeE)-1)
e = muligeE[indeks]

lock = (e, n)
print(f"Låsen er {lock}")

d = randint(1,3) * (phi - 1)
# d må være slik at e*d % phi = 1
key = (e * d, phi)
print((f"d % phi = {key[0] % phi}"))
print(f"Nøkkelen er {key}")

# Kryptering:

Melding = 3
c = (Melding ** lock[0]) % lock[1]

# Dekryptering:
M = (c ** key[0]) % key[1]

print(f"E={e}, d={d}, c={c}, Meldingen er {M}")