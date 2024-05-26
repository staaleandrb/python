
For å lese gjennom filen og telle bokstaver med kun én løkke, kan du bruke en itererbar måte å lese filen direkte i en løkke. Her er en måte å gjøre det på:

python
Kopier kode
alfa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
antall = [0] * len(alfa)  # Initialiserer telleren til null for hver bokstav

def read_file(filnavn):  # Åpner fila og leser innholdet av fila
    f = open(filnavn, "r")  # Bruker 'with' for å sikre at filen lukkes korrekt
    for char in f  # Leser hele filen og itererer gjennom hvert tegn
        print(char)
        #if char in alfa:
        #    antall[alfa.index(char)] += 1  # Øker telleren for riktig bokstav
    
    print(antall)

# Eksempel på bruk
read_file("kryptering/caesarsChiffer/kryptert.txt")