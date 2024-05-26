alfa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
antall = [0] * len(alfa)  # Initialiserer telleren til null for hver bokstav

def read_file(filnavn):  # Åpner fila og leser innholdet av fila
    f = open(filnavn, "r")  # Bruker 'with' for å sikre at filen lukkes korrekt
    for tekst in f:  # Leser hele filen og itererer gjennom hvert tegn
        for bokstav in tekst:
            if bokstav in alfa:
                antall[alfa.index(bokstav)] += 1
    skriut()
    
def skriut():
    for i in range(len(alfa)):
        print(alfa[i], antall[i])
    

read_file("kryptering/caesarsChiffer/kryptert.txt")