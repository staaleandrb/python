alfa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
antall = [0] * len(alfa)  # Initialiserer telleren til null for hver bokstav

def read_file(filnavn):  # Åpner fila og leser innholdet av fila
    with open(filnavn, "r") as f:  # Bruker 'with' for å sikre at filen lukkes korrekt
        for line in f:  
            for char in line.lower():  # Konverterer til små bokstaver
                if char in alfa:
                    antall[alfa.index(char)] += 1  # Øker telleren for riktig bokstav
    print(antall)

# Eksempel på bruk
read_file("kryptering/caesarsChiffer/kryptert.txt")
