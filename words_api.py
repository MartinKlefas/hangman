import rapidAPICredentials
import random


import requests

def get_words_list():
    try:
        url = "https://wordsapiv1.p.rapidapi.com/words/"

        querystring = {"letterPattern":"^[a-zA-Z]+","limit":"10","page":random.randint(1,3376),"frequencymin":"4"}

        headers = {
            'X-RapidAPI-Key': rapidAPICredentials.key,
            'X-RapidAPI-Host': rapidAPICredentials.host
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        jsonResponse = response.json()
        results = jsonResponse['results']['data']

        return results
    except:
        return ["Apple","Banana","Pear","Orange","Plum"]
