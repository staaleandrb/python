# Denne er ikke ferdig.

#Hvordan ble Maria Stuart avslørt? 
#Jo, de som løste koden hennes brukte noe som kalles frekvensanalyse. 
#Noen bokstaver er mye vanligere enn andre i et gitt språk. 
#lista frekvens nedenfor viser bokstavene i det norske alfabetet, 
# og hvor ofte de forekommer i vanlige tekster i posent. 
#Med frekvensanalyse kan vi undersøke hvor ofte ulike tegn forekommer i en kryptert tekst,
# og dermed finne ut hvilke tegn som koder for hvilke bokstaver. 
#Det forutsetter at en form for substitusjonskryptering er brukt, 
#slik som den som ble brukt av Maria Stuart.


#Kan du dekryptere tekstene ved hjelp av frekvensanalyse? 


frekvens =[6.07,1,47,0.34,4.21,15.38,2.02,3.90,1.64,6.16,1.02,3.83,5.26,3.40,7.81,5.03,2.06,0.02,8.53,6,36,7.84,1.80,2.40,0.15,0.05,0.74,0.04,0.20,0.76,1.50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 

alfa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
antall = [0] * len(alfa)  # Initialiserer telleren til null for hver bokstav
prosent = [0] * len(alfa)  # Initialiserer prosenten til null for hver bokstav

def read_file(filnavn):  # Åpner fila og leser innholdet av fila
    f = open(filnavn, "r")  # Bruker 'with' for å sikre at filen lukkes korrekt
    for tekst in f:  # Leser hele filen og itererer gjennom hvert tegn
        for bokstav in tekst:
            if bokstav in alfa:
                antall[alfa.index(bokstav)] += 1
    finnProsent()
    desifre()
    #skriut()

def finnProsent():  # Finner prosenten av hver bokstav
    for i in range(len(alfa)):
        prosent[i] = (antall[i] / sum(antall)) * 100
        prosent[i] = round(prosent[i], 2)

def skriut():
    print("Bokstav | Antall | Prosent | NorskFrekvens")
    for i in range(len(alfa)):
        print(alfa[i], antall[i], prosent[i],frekvens[i])

def desifre():
    #print("sortert liste", organiser_alfa(alfa, prosent))
    
    sortert_alfa = organiser_alfa(alfa, prosent)
    print("sortert liste", sortert_alfa)


def organiser_alfa(alfa, frekvens):
    # Kombinerer alfa og frekvens til par av bokstav og frekvens
    bokstav_frekvens_par = zip(alfa, frekvens)
    # Sorterer par basert på frekvens
    sortert_par = sorted(bokstav_frekvens_par, key=lambda x: x[1])
    # Trekker ut bokstavene fra sorterte par
    sortert_alfa = [par[0] for par in sortert_par]
    return sortert_alfa

def skrivTilFil(innhold): # Skriver til fil. Om den ikke finnes så blir den opprettet
    f= open("kryptering/caesarsChiffer/svar.txt","w+")
    f.write(innhold) 
    f.close


read_file("kryptering/caesarsChiffer/kryptert.txt")