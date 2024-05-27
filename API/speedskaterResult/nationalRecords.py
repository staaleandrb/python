import requests

# URL for weather data (note: the URL provided seems to be for speedskating records, not weather data)
url = "https://speedskatingresults.com/api/json/country_records.php"

# Parameters for the request
params = {
    "country": "NOR",

    "distance": "500",
    
    "gender": "f",

    "age": "sr"
}

# Make the GET request with the parameters
responseCountry = requests.get(url, params=params)

# Print the JSON response
print(responseCountry.json())
