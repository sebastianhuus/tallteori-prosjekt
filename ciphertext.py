from bokstaver import småbokstaver, storebokstaver


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
