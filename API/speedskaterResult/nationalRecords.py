# Laget av : Staale Andre Bergersen
import requests

# URL for weather data (note: the URL provided seems to be for speedskating records, not weather data)
url = "https://speedskatingresults.com/api/json/country_records.php"
urlWordRecord = "https://speedskatingresults.com/api/json/world_records.php"
urlPersonalRecord = "https://speedskatingresults.com/api/json/personal_records.php"
urlTrackRecord = "https://speedskatingresults.com/api/json/track_records.php"

# Parameters for the request
Opg1 = {
    "country": "NOR",

    "distance": "500",
    
    "gender": "f",

    "age": "sr"
}

opg2 = {
    "country": "NOR",

    "distance": "10000",

    "gender": "m",

    "age": "sr"

}

opg3 = {
    "gender": "m",
    "age": "sr",
    "distance": "500"
}

opg4 = {
    "skater": "695",
    "distance": "10000"
}

opg5 = {
    "track": "73"
}

opg6Nor = {
    "country": "NOR"
}
# Make the GET request with the parameters
responseOpg1 = requests.get(url, params=Opg1)
responseOpg2 = requests.get(url, params=opg2)
responseOpg3 = requests.get(urlWordRecord, params=opg3)
responseOpg4 = requests.get(urlPersonalRecord, params=opg4)
responseOpg5 = requests.get(urlTrackRecord, params=opg5)
responseOpg6Verden = requests.get(urlWordRecord)
responseOpg6Norge = requests.get(url,params=opg6Nor)
# Print the JSON response

KvinneNor500 = responseOpg1.json()
MannNor10000 = responseOpg2.json()
MenVerdenrekord500 = responseOpg3.json()
JohanOlavKoss10000 = responseOpg4.json()
SkienBanerekord = responseOpg5.json()
verden= responseOpg6Verden.json()
norge = responseOpg6Norge.json()


def convert_to_seconds(time_str):
    parts = time_str.split('.')
    if len(parts) == 3:
        minutes = int(parts[0])
        seconds = int(parts[1])
        hundredths = int(parts[2])
        return minutes * 60 + seconds + hundredths / 100
    elif len(parts) == 2:
        seconds = int(parts[0])
        hundredths = int(parts[1])
        return seconds + hundredths / 100
    else:
        return float(time_str)

print("#1 Hvem er Norges raskeste kvinne på 500 meter.")
print(KvinneNor500['records'][0]['skater']['givenname'], KvinneNor500['records'][0]['skater']['familyname'])
print("#2. Hvem er Norges raskeste mann på 10 000 meter og hvor fort gikk han?")
print(MannNor10000['records'][0]['skater']['givenname'], MannNor10000['records'][0]['skater']['familyname'], MannNor10000['records'][0]['time'])
print("#3. Hva er verdenrekorden på 500m menn? Hva heter han?")
print(MenVerdenrekord500['records'][0]['time'], MenVerdenrekord500['records'][0]['skater']['givenname'], MenVerdenrekord500['records'][0]['skater']['familyname'])
print("#4. Hva er den personlige rekorden til Johan Olav Koss på 10 000 meter.")
print(JohanOlavKoss10000['records'][0]['time'])
print("#5. Hva er banerekordene satt Skien. Hvem har dem?")

for i in range(0, len(SkienBanerekord['records'])):  
   print(SkienBanerekord['records'][i]['gender'],SkienBanerekord['records'][i]['distance'], SkienBanerekord['records'][i]['skater']['givenname'], SkienBanerekord['records'][i]['skater']['familyname'], SkienBanerekord['records'][i]['time'])

print("#6. Hvor stor er differansen mellom Verdensrekorden og Norgesrekorden for menn på de enkelte distansene. Pressenter tallene og differansen på en god måte.")

world_records_dict = {(rec['distance'], rec['gender']): rec for rec in verden['records']}
norwegian_records_dict = {(rec['distance'], rec['gender']): rec for rec in norge['records']}

for key in world_records_dict:
    if key in norwegian_records_dict:
        world_time_str = world_records_dict[key]['time'].replace(',', '.')
        norwegian_time_str = norwegian_records_dict[key]['time'].replace(',', '.')
        world_time = convert_to_seconds(world_time_str)
        norwegian_time = convert_to_seconds(norwegian_time_str)
        difference = norwegian_time - world_time
        print(f"Distansen: {key[0]}m, Kjønn: {key[1]}, Verdensrekord: {world_time_str}, Norgesrekord: {norwegian_time_str}, Forskjell: {difference:.2f} sekunder")