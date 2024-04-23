"""
# Oppgave: Beregne lønn

Du skal lage tre klasser i Python: Person, Ansatt og Leder.

Person er det overordnede klassen som Leder og ansatt skal arve ifra. Denne klassen må derfor innea de egenskaper og metoder som er felles.
 Jobber du som leder i dette firma har du en særegen bonusordning. 
 Hver leder for en prosentandel av det totale årlige overskuddet til bedriften.
   Dette gjør ikke de øvrige ansatte. Bruk Python og objekt orienter programmering til å løse problemstillingen.

Person-klassen skal ha følgende egenskaper og metoder:

Egenskaper

Navn

Navn

Id

Timelønn

Metoder:

EndreLonn()

Ansatt-klassen skal ha følgende egenskaper og metoder:

Metoder:

__init__: En konstruktør som tar imot navn, ansatt ID og timelønn som parametere

og oppretter en ny ansatt med disse verdiene.

beregn_lønn(self, antall_timer): En metode som tar imot antall timer jobbet og returnerer lønnen basert på timelønnen til den ansatte.

SkrivUt()

Denne metoden skal arve en metode fra superklassen og i tillegg skrive ut det som er spesielt for denne klassen. Dvs det regnes ikke ut bonus.

Leder-klassen skal arve fra person-klassen og ha følgende egenskaper og metoder:

Egenskaper:

Bonusandel (prosent av basislønn)

Metoder:

__init__: En konstruktør som tar imot navn, ansatt ID, timelønn og bonusandel som parametere og oppretter en ny leder med disse verdiene.

beregn_lønn(self, antall_timer): En metode som tar imot antall timer jobbet og returnerer lønnen til lederen, som er summen av baselønnen og bonusen basert på bonusandelen.

Skriv ut()

Skriver ut som i classen ansatt.

Bonusoppgave:

Legg til en metode i både Ansatt- og Leder-klassene som lar deg endre timelønnen for en ansatt.

Lykke til med oppgaven!

"""

from leder import leder
from ansatt import ansatt


# lager objekter
ansatt1 = ansatt("Ole", 1, 100)
ansatt2 = ansatt("Dole", 2, 200)
ansatt3 = leder("Doffen", 3, 250,3)

#ansatt1.skrivUt()
#ansatt3.skrivUt()

print(ansatt1.regnUtLonn(20))  # sender inn 10 arbeidtimer
print(ansatt3.regnUtLonn(10))  # sender inn 10 arbeidtimer