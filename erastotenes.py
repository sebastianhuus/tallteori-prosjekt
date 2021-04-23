lim = 100
list = []
n = lim + 1

for i in range(2, n):
    list.append(i)

# primtallet
prime = 2

# liste over alle primtall vi finner, starter med 2
primes = [2]

multiples = []
lum = []

# finner alle produkter av primtallet og legger dem i en ny liste
for i in range(2, n):
    multiples.append(i*prime)

# fjerner primtallsproduktet fra hovedlista
for i in range(len(multiples)):
    if multiples[i] in list:
        list.remove(multiples[i])

# neste primtallet er det minste tallet som er større enn det nåværende primtallet
for i in range(len(list)):
    if i > prime:
        prime = i
        break
