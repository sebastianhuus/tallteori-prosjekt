
# lim er det siste tallet i intervallet vi undersøker
lim = 1000

# Hjelpeliste for å holde alle tallene i intervallet
alletall = []

# Bruker en hjelpevariabel for å telle.
n = lim + 1

# Legger til alle tall i intervallet
for i in range(2, n):
    alletall.append(i)

# Starter på 2, det minste primtallet
primtall = 2

# Hjelpeliste for å holde alle primtallene våre.
alleprimtall = [2]

def fjern_multiplum(tallListe, tall):
    # Hjelpeliste for å holde alle tallene i n-gangen, hvor n er det nåværende primtallet.
    multiplum = []

    # Lager lokal kopi av lista så vi ikke smasher den originale
    tallListe = tallListe

    # Finner alle produkter av primtallet og legger dem i en ny liste
    for i in range(2, n):
        multiplum.append(i * tall)

    # fjerner primtallsproduktet fra hovedlista
    for i in range(len(multiplum)):
        if multiplum[i] in alletall:
            tallListe.remove(multiplum[i])

    return tallListe


# neste primtallet er det minste tallet som er større enn det nåværende primtallet
def finn_neste_primtall(liste, tall):
    for nyttTall in liste:
        if nyttTall > tall:
            return nyttTall


counter = 0
while True:
    try:
        alletall = fjern_multiplum(alletall, alleprimtall[counter])
        nyttPrimtall = finn_neste_primtall(alletall, alleprimtall[counter])
    except (ValueError, TypeError):
        break

    if nyttPrimtall is None:
        break

    alleprimtall.append(nyttPrimtall)
    counter += 1

print(alleprimtall)
