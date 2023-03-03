import http.client

conn = http.client.HTTPSConnection("wordsapiv1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "ad5b420f13msh656a9fd969677dfp1567a7jsn1fb476f1cada",
    'X-RapidAPI-Host': "wordsapiv1.p.rapidapi.com"
    }

conn.request("GET", "/words/?letterPattern=%5E%5Ba-zA-Z%5D%2B&limit=100&page=1&hasDetails=hasDetails", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
