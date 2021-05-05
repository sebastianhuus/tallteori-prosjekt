# encoding=utf-8

# det er 50-50 mellom norsk og engelsk fordi ya boi can't decide on a language
from primtall import liste as alleprimtall


def finn_faktorer(tall):
    faktorer = []

    for primtall in alleprimtall:
        if tall % primtall == 0:
            faktorer.append(primtall)

    return faktorer


def finn_største_tall(liste):
    størst = 0
    for tall in liste:
        if tall > størst:
            størst = tall
    return størst


def finn_sff(tall1, tall2=None):
    # Returnerer største faktor til ett tall som vi gir funksjonen.
    if tall2 is None:
        sff = finn_største_tall(finn_faktorer(tall1))
        if sff == tall1:
            return 1
        else:
            return sff

    # Returnerer SFF mellom to tall.
    # Vi trenger bare faktorene til det ene tallet. Har ikke noe å si om a er større enn b. SFF is eternal.
    faktorer = finn_faktorer(tall1)

    fellesfaktorer = []
    for faktor in faktorer:
        if tall2 % faktor == 0:
            fellesfaktorer.append(faktor)

    # SFF er et produkt av fellesfaktorene. Dette regnes ut under.
    sff = 1
    for fellesfaktor in fellesfaktorer:
        sff *= fellesfaktor

    return sff
