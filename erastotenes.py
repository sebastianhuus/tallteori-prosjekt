# Denne algoritmen finner primtall.
# Algoritmen er modellert etter hvordan man gjør det for hånd

# Funksjonen skaffer en liste over absolutt alle tall i intervallet vårt.
def lag_talliste(n):
    liste = []

    # Legger til alle tall i intervallet
    for i in range(2, n + 1):
        liste.append(i)

    return liste


# Fjerner alle multiplum av et gitt tall. Feks n=2, så tar den ut 4,6,8,10 etc.
def fjern_multiplum(tallListe, tall, n):
    # Hjelpeliste for å holde alle tallene i "p-gangen", hvor p er det nåværende primtallet.
    multiplum = []

    # Lager lokal kopi av lista så vi ikke smasher den originale
    liste = tallListe

    # Finner alle produkter av primtallet og legger dem i en ny liste
    for i in range(2, n + 1):
        multiplum.append(i * tall)

    # fjerner primtallsproduktet fra hovedlista
    for i in range(len(multiplum)):
        if multiplum[i] in alletall:
            liste.remove(multiplum[i])

    return liste


# Det neste primtallet er det minste tallet som er større enn det nåværende primtallet.
# Hvis n=2, vil det neste tallet være 3 siden vi har fjernet alle tall 2*k. Dermed blir lista [2,3,5,7,...]
def finn_neste_primtall(liste, tall):
    for nyttTall in liste:
        if nyttTall > tall:
            return nyttTall


# ------------main loop------------
# lim er det siste tallet i intervallet som vi undersøker
lim = 1000

# Hjelpeliste for å holde alle tallene i intervallet
alletall = lag_talliste(lim)

# Hjelpeliste for å holde alle primtallene våre. Starter på 2
alleprimtall = [2]

counter = 0  # teller indekset av det nåværende primtallet i primtallslista
while True:
    try:
        alletall = fjern_multiplum(alletall, alleprimtall[counter], lim)
        nyttPrimtall = finn_neste_primtall(alletall, alleprimtall[counter])
    except (ValueError, TypeError):
        break

    if nyttPrimtall is None:
        break

    alleprimtall.append(nyttPrimtall)
    counter += 1

print(alleprimtall)
