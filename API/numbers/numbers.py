import requests as req
 
number = input("Enter a number: ")

url = f"http://numbersapi.com/{number}?json"

result = req.get(url)

print(f"Status code: {result.status_code}")