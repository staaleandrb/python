# Dette skriptet sender en forespørsel til MET API-et for å hente værdata for Oslo. 

import requests

# Angi URL for værdata
url = "https://api.met.no/weatherapi/locationforecast/2.0/compact"

# Angi dine koordinater (latitude, longitude)

params = {          # Porsgrunn koordinater
    "lat": 59.14,  
    "lon": 9.65
}

# identifiser deg som bruker
headers = {
    "User-Agent": "https://github.com/staaleandrb/"
}

# Send GET-forespørselen
response = requests.get(url, params=params, headers=headers)
data = response.json()
timeseries = data['properties']['timeseries'] # Henter ut tidsserien

# Skriv ut temperatur for de neste 10 tidspunktene
for i in range(1, 11):
    print(timeseries[i]['data']['instant']['details']['air_temperature']) # Skriver ut første element i tidsserien
