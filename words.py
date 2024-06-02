import http.client
def get_words():
    try:
        conn = http.client.HTTPSConnection("wordsapiv1.p.rapidapi.com")

        headers = {
            'X-RapidAPI-Key': "key",
            'X-RapidAPI-Host': "wordsapiv1.p.rapidapi.com"
            }

        conn.request("GET", "/words/?letterPattern=%5E%5Ba-zA-Z%5D%2B&limit=100&page=1&hasDetails=hasDetails", headers=headers)

        res = conn.getresponse()
        data = res.read()
        
        conn.close()

        return(data.decode("utf-8"))
    except:
        return["Apple","Banana","Pear","Orange","Plum"]
