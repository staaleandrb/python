# Denne filen skal lese inn data fra en JSON-fil og opprette objekter basert på dataene.
# Dette for å kunne bruke de ulike metodene i klassene 



import json
from prosessor import Prosessor
from ram import Ram
import os
from objekter import komponenter

kategorier = []

for objekt in komponenter:
    kategori = objekt.get("kategori")
    if kategori not in kategorier:
        kategorier.append(kategori) 

print("Kategorier:", kategorier)  # Skriver ut kategoriene


 # Gå gjennom hvert objekt i listen
for objekt in komponenter:
    # Sjekk om kategorien finnes i listen over kategorier
    if objekt.get("kategori") in kategorier:
        # Opprett en instans av Ram-klassen med objektets data
        
        
print(kategori)


"""
        objekt_klasse = eval(objekt["kategori"]).viskomponent(self)
        del objekt["kategori"]
        temp = objekt_klasse(**objekt)

        temp.vis_komponent()
        # for x in range(len(kategorier)):       
        #     temp = kategorier[x]

        #     komponent = eval(temp).vis_komponent()
        #     x+=1 
        
        # Bruk vis_komponent-metoden på den opprettede instansen
          #  komponent.vis_komponent()
"""