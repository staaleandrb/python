# Dette skriptet sender en forespørsel til MET API-et for å hente værdata for Oslo. 

import requests

# Angi URL for værdata
url = "https://api.met.no/weatherapi/locationforecast/2.0/compact"

# Angi dine koordinater (latitude, longitude)

porsgrunn = {          # Porsgrunn koordinater
    "lat": 59.14,  
    "lon": 9.65
}

bodo = {          # Porsgrunn koordinater
    "lat": 67.32,  
    "lon": 14.34
}

# identifiser deg som bruker
headers = {
    "User-Agent": "https://github.com/staaleandrb/"
}

# Send GET-forespørselen
responsePorsgrunn = requests.get(url, params=porsgrunn, headers=headers)
responseBodo = requests.get(url, params=bodo, headers=headers)
dataPorsgrunn = responsePorsgrunn.json()
dataBodo = responseBodo.json()

timeseriesPorsgrunn = dataPorsgrunn['properties']['timeseries'] # Henter ut tidsserien Porsgrunn
timeseriesBodo = dataBodo['properties']['timeseries'] # Henter ut tidsserien Bodø

# Skriv ut temperatur for de neste 10 tidspunktene
print("Porsgrunn: Bodø:")
for i in range(1, 11):
   print(f"{timeseriesPorsgrunn[i]['data']['instant']['details']['air_temperature']} ", 
      f"{timeseriesBodo[i]['data']['instant']['details']['air_temperature']}")