"""
# UV Oppgave – Objektorientert programmering: PC-komponenter

I denne oppgaven skal du, som programmerer, hjelpe en person som selger brukte PC-komponenter. 
Med PC-komponenter mener vi deler som finnes inne i en PC. 
Han ønsker på sikt lage et dataprogram med objektorientert programmering for å kunne registrerer alle PC-komponenter han får inn som han igjen skal selge.

Du får i oppdrag å lage et forslag til hvilke klasser med objekt-verdier (properties) og med objekt-funksjoner (metoder) som er nødvendige.

Tips! Tenk at du skal samle all informasjon som er generell, det vil si gyldig for alle typer komponenter, i en superklasse. 
Lag så mange subklasser du trenger som igjen skal arve både objekt-verdier (properties) og objekt-funksjoner (metoder) fra superklassen.
I subklassene skal du registrerer det som er spesielt for hver enkelt PC-komponent.

Du skal opprette to objekter fra hver subklasse. 
Alle objekter skal legges til i en liste. Alle elementer (objekter) i listen skal skrives ut med en løkke ved hjelp av den samme metoden «vis_komponent».

Programmet skal skrives i Python



"""    

from prosessor import Prosessor
from ram import Ram

prosessor1 = Prosessor("Intel i7", 2000, 8, 3.6)
prosessor2 = Prosessor("AMD Ryzen 5", 1500, 6, 3.2)

prosessor1.vis_komponent()