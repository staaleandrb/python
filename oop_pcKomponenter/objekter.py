"""
#Utvidelse av oppgaven:

Etter å ha implementert klassene og objektene i Python, skal elevene utvide programmet med følgende funksjonaliteter:

Lag en metode for å filtrere komponenter etter pris:
Lag en funksjon som tar inn en liste av komponentobjekter og et prisintervall som parameter.
Funksjonen skal returnere en ny liste med komponenter som faller innenfor det angitte prisintervallet.

Legg til funksjonalitet for å oppdatere komponentpriser:
Lag en metode i hver klasse for å oppdatere prisen på en komponent.
Denne metoden skal ta inn den nye prisen som parameter og oppdatere prisen på komponenten.

Implementer funksjonalitet for å finne den dyreste komponenten:
Lag en funksjon som tar inn en liste av komponentobjekter som parameter.

Funksjonen skal returnere den dyreste komponenten i listen.
Legg til støtte for å lagre og laste komponenter til/fra en fil:

Implementer funksjoner for å lagre komponenter til en tekstfil og for å laste komponenter fra en tekstfil.
Formatet på filen kan være enkel tekst eller CSV.

Bygg et brukergrensesnitt:
Utvikle et enkelt brukergrensesnitt ved hjelp av biblioteker som Tkinter eller PyQt.
Brukergrensesnittet bør tillate brukere å legge til nye komponenter, oppdatere eksisterende komponenter, filtrere komponenter etter pris, og vise den dyreste komponenten.
Oppfordre elevene til å bruke kommentarer for å forklare koden der det er nødvendig, og til å teste programmet grundig etter hver implementering.
"""    
import json
from prosessor import Prosessor
from ram import Ram
import os

# Bestem den absolutte banen til filen basert på den gjeldende arbeidsmappen
mappebane = os.path.dirname(os.path.abspath(__file__))
filbane = os.path.join(mappebane, "komponenter.json")

print("Filbane:", filbane)  # Feilsøkingsutskrift

# Opprett en tom liste for komponenter
komponenter = []

# Les innholdet fra .json-filen, hvis den eksisterer
try:
    with open(filbane, "r") as json_file:
        komponenter = json.load(json_file)
except FileNotFoundError:
    # Håndter hvis filen ikke finnes
    print("Filen 'komponenter.json' ble ikke funnet. En ny fil vil bli opprettet.")


# Lag nye objekter
prosessor1 = Prosessor("Intel i8", 2000, 8, 3.6)
prosessor2 = Prosessor("AMD Ryzen 5", 1500, 6, 3.2)

# Legg til de nye objektene i listen av komponenter
komponenter.append(prosessor1.to_dict())
komponenter.append(prosessor2.to_dict())
""""
ram1 = Ram("Corsair Vengeance", 800, 16, 3200)
ram2 = Ram("Kingston HyperX", 600, 8, 2666)



komponenter.append(ram1.to_dict())
komponenter.append(ram2.to_dict())

"""

# Skriv den oppdaterte listen til .json-filen
with open(filbane, "w") as json_file:
    json.dump(komponenter, json_file, indent=4)
