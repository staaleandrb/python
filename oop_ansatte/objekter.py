
"""""

Oppgave: Ansatt- og Leder-klasser

Du skal lage to klasser i Python: Ansatt og Leder.

Ansatt-klassen skal ha følgende egenskaper og metoder:

Egenskaper:
Navn
Ansatt ID
Timelønn
Metoder:
__init__: En konstruktør som tar imot navn, ansatt ID og timelønn som parametere 
og oppretter en ny ansatt med disse verdiene.
beregn_lønn(self, antall_timer): En metode som tar imot antall timer jobbet og returnerer lønnen basert på timelønnen til den ansatte.
Leder-klassen skal arve fra Ansatt-klassen og ha følgende egenskaper og metoder:

Egenskaper:
Bonusandel (prosent av basislønn)
Metoder:
__init__: En konstruktør som tar imot navn, ansatt ID, timelønn og bonusandel som parametere og oppretter en ny leder med disse verdiene.
beregn_lønn(self, antall_timer): En metode som tar imot antall timer jobbet og returnerer lønnen til lederen, som er summen av baselønnen og bonusen basert på bonusandelen.
Skriv deretter en enkel testklient som oppretter noen ansatte og ledere, beregner lønn for dem ved å kalle beregn_lønn-metoden, og skriver ut lønnen.

Bonusoppgave:
Legg til en metode i både Ansatt- og Leder-klassene som lar deg endre timelønnen for en ansatt.

Lykke til med oppgaven! Hvis du har noen spørsmål underveis, er jeg her for å hjelpe deg.

"""  
from leder import leder
from ansatt import ansatte

ansatt1 = leder("Ola", 1, 100,2)
ansatt2 = leder("Kari", 2, 200,3)
ansatte3 = ansatte("Per", 3, 300)


print(ansatt1.beregn_lønn(1200))

ansatte3.endreLon(500)