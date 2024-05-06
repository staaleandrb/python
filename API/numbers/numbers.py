import requests as req
 
url = "http://numbersapi.com/100?json"
 
resultat = req.get(url)
 
print(f"Statuskode: {resultat.status_code}")
 
data = resultat.json()
 
print(data)
"""print(data["text"])"""