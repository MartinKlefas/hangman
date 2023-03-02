import http.client

conn = http.client.HTTPSConnection("wordsapiv1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': 
    'X-RapidAPI-Host': "wordsapiv1.p.rapidapi.com"
    }

conn.request("GET", "/words/?letterPattern=%5Ba-zA-Z%5D*&partofspeech=noun&lettersmin=5&lettersMax=8&limit=10&page=1&frequencymin=3", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
