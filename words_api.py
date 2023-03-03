import http.client
import rapidAPICredentials


conn = http.client.HTTPSConnection("wordsapiv1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': rapidAPICredentials.key,
    'X-RapidAPI-Host': rapidAPICredentials.host
    }

conn.request("GET", "/words/?letterPattern=%5E%5Ba-zA-Z%5D%2B&lettersmin=4&letters=8&limit=10&page=1&frequencymin=5", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))